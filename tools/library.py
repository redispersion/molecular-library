"""Small stdlib-only interface to the local molecular library."""
from pathlib import Path
import argparse
import hashlib
import json
import shutil

ROOT = Path(__file__).resolve().parents[1]

def read(relative):
    return json.loads((ROOT/relative).read_text())

def sha(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda:f.read(1024*1024),b''):
            h.update(block)
    return h.hexdigest()

parser=argparse.ArgumentParser(description=__doc__)
sub=parser.add_subparsers(dest='command',required=True)
sub.add_parser('list')
sub.add_parser('verify')
ex=sub.add_parser('export',help='Copy an immutable model snapshot into a new project directory; does not resolve FF dependencies.')
ex.add_argument('model',help='Relative model path, as printed by list')
ex.add_argument('destination',type=Path)
args=parser.parse_args()
if args.command=='list':
    for m in read('catalog/models.json'):
        print(f"{m['path']}  [{m['status']}]")
elif args.command=='verify':
    problems=[]
    objects=read('catalog/objects.json')
    files=read('catalog/files.json')
    for obj in objects:
        p=ROOT/'objects/sha256'/obj['sha256'][:2]/obj['sha256']
        if not p.is_file() or sha(p)!=obj['sha256']:
            problems.append(f'Object missing/changed: {p}')
    for f in files:
        p=ROOT/f['path']
        target=ROOT/'objects/sha256'/f['sha256'][:2]/f['sha256']
        if not p.is_symlink() or p.resolve()!=target.resolve() or not p.is_file():
            problems.append(f'Broken or redirected link: {p}')
    for m in read('catalog/models.json'):
        meta=read(f"{m['path']}/model.json")
        for f in meta['files']:
            p=ROOT/m['path']/f['name']
            if not p.is_file() or sha(p)!=f['sha256']:
                problems.append(f'Model manifest mismatch: {p}')
    if problems:
        raise SystemExit('\n'.join(problems))
    print(f"OK: {len(objects)} objects, {len(files)} file links; all model manifests verified.")
elif args.command=='export':
    models={m['path'] for m in read('catalog/models.json')}
    if args.model not in models:
        raise SystemExit('Unknown model path; use list.')
    meta=read(f'{args.model}/model.json')
    base=ROOT/args.model
    for f in meta['files']:
        if sha(base/f['name'])!=f['sha256']:
            raise SystemExit('Source checksum mismatch; export aborted.')
    if args.destination.exists():
        raise SystemExit('Destination already exists; refusing to overwrite.')
    args.destination.mkdir(parents=True)
    for f in meta['files']:
        shutil.copyfile(base/f['name'],args.destination/f['name'])
    snapshot={'library_model':args.model,'source_library':str(ROOT),'model':meta,
        'note':'This is a materialized model snapshot, not a complete simulation system. Resolve forcefield dependencies separately.'}
    (args.destination/'model-selection.json').write_text(json.dumps(snapshot,ensure_ascii=False,indent=2)+'\n')
    print(f"Exported {len(meta['files'])} real files to {args.destination}")
    print('Force-field dependency status:',meta['forcefield_dependency']['status'])
