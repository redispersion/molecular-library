# Результат первичной инвентаризации, 2026-11-13

Найдено 739 файлов подходящих расширений в проверенных каталогах.
Из них 219 файлов вне программных дистрибутивов проверены по SHA256.
Создано 14 записей моделей; 12 каталогов молекул/фрагментов/комплексов.
Фактически хранится 70 уникальных файлов (4492785 байт),
на них ссылаются 78 именованных путей.
В источниках найдено 27 групп побайтовых дублей.

Это техническая инвентаризация, не физическая валидация силовых полей.

## Импортированные модели

| Молекула/фрагмент | Модель | Координаты и ITP |
|---|---|---|
| 5cb | [gromos54a7-atb-32350](../molecules/5cb/models/gromos54a7-atb-32350/v1/model.json) | имена/порядок совпадают |
| 5cb | [gromos54a7-atb-569019](../molecules/5cb/models/gromos54a7-atb-569019/v1/model.json) | имена/порядок совпадают |
| 5cb | [acpype-legacy](../molecules/5cb/models/acpype-legacy/v1/model.json) | имена/порядок совпадают |
| chlorophyll-a | [atb-legacy-0bonds-label](../molecules/chlorophyll-a/models/atb-legacy-0bonds-label/v1/model.json) | имена/порядок совпадают |
| chlorophyll-a | [atb-legacy-2bonds-label](../molecules/chlorophyll-a/models/atb-legacy-2bonds-label/v1/model.json) | имена/порядок совпадают |
| chlorophyll-a | [atb-legacy-4bonds-label](../molecules/chlorophyll-a/models/atb-legacy-4bonds-label/v1/model.json) | имена/порядок совпадают |
| ethanol | [atb-legacy](../molecules/ethanol/models/atb-legacy/v1/model.json) | имена/порядок совпадают |
| n-hexane | [atb-legacy](../molecules/n-hexane/models/atb-legacy/v1/model.json) | имена/порядок совпадают |
| pibma-head | [legacy](../molecules/pibma-head/models/legacy/v1/model.json) | имена/порядок совпадают |
| pibma-body | [legacy](../molecules/pibma-body/models/legacy/v1/model.json) | имена/порядок совпадают |
| pibma-tail | [legacy](../molecules/pibma-tail/models/legacy/v1/model.json) | имена/порядок совпадают |
| pibma-monomer | [legacy](../molecules/pibma-monomer/models/legacy/v1/model.json) | имена/порядок совпадают |
| pibma-chain | [legacy](../molecules/pibma-chain/models/legacy/v1/model.json) | имена/порядок совпадают |
| water | [legacy-spce](../molecules/water/models/legacy-spce/v1/model.json) | требуется preprocessing/проверка |

## Важные результаты

- Оба новых комплекта 5CB ATB: 38 атомов, общий заряд 0, соответствие PDB/ITP по именам и порядку подтверждено.
- Старый локальный GROMOS54A7-ATB не содержит типов `COpt`, `C_H3`, `HCAr`, `HCH3`, `HOpt`, `NItr`, нужных новым 5CB ITP. Нужна соответствующая базовая выгрузка ATB; старый FF не объявлен рабочей зависимостью.
- Chl a: имена 0/2/4bonds сохранены как исходные метки. Фактически Mg имеет 2/2/4 явно заданных соседей соответственно; это записано в model.json.
- Водная топология содержит альтернативные preprocessor-ветки. Простой разбор видит повторные atom indices; сравнение откладывается до preprocessing. Это не утверждение о наличии шести физических атомов в воде.
- `NMA.itp` содержит 7128 записей atoms; сохранён в incoming, а не объявлен моделью небольшой молекулы. Химическая идентичность не установлена.
- Исходный неполный `chlA.gro` (81 запись при заголовке 137) сохранён в quarantine; обе найденные копии перечислены в каталоге происхождения.
- Старые черновики Chl a–ацетонитрил — только архив геометрий, не одобренные расчётные задания.
- Нестандартные/нечисловые координаты в диагностических результатах отмечены в inventory.json. Эти файлы не импортированы как библиотечные молекулы.
- Новые записи не подтверждают работоспособность всей GROMACS-системы. Совместимость базового FF, параметры Mg и физические свойства проверяются отдельно.

## Область поиска

Точные корни и ограничения: [scan.json](scan.json). Полный список: [inventory.json](inventory.json).
Дубли: [duplicates.json](duplicates.json). Источники каждого объекта: [objects.json](objects.json).
Программные примеры/дистрибутивы и собранные системы только проиндексированы.
Все исходные файлы оставлены на месте. Облачная выгрузка не выполнялась.
