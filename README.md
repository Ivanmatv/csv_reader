# CSV Data Reader

Проект предоставляет утилиту для обработки CSV-файлов с возможностью фильтрации и агрегации данных.

## Функционал

- Чтение CSV-файлов
- Фильтрация данных по условиям (`>`, `<`, `=`, `>=`, `<=`)
- Агрегация данных (среднее, минимум, максимум)
- Красивый вывод в виде таблиц с помощью `tabulate`

## Примеры запуска приложения 

1. Вывод таблицы из файла 
```bash
python main.py --file test_file.csv
```
2. Фильтрация данных
```bash
python main.py --file test_file.csv --where "rating>4.7"
```
3. Агрегация данных (средний рейтинг)
```bash
python main.py --file data.csv --aggregate "rating=avg"
```
4. Комбинирование фильтрации и агрегации
```bash
python main.py --file data.csv --where "rating>4.7" --aggregate "rating=avg"
```
5. Запуск теста
```bash
pytest test_main.py -v
```