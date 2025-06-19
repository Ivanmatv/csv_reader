import csv
import argparse

from tabulate import tabulate


def read_csv(file_path: str) -> list:
    """Чтение CSV файла."""
    with open(file_path, newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        return [row for row in reader]


def filter_csv(data: list, condition: str) -> list:
    """Фильтрация данных по условию."""
    column, operator, value = condition.split()
    value = value.strip()

    column_index = None
    for i, header in enumerate(data[0]):
        if header == column:
            column_index = i
            break

    if operator == ">":
        return [row for row in data[1:] if float(row[column_index]) > float(value)]
    elif operator == "<":
        return [row for row in data[1:] if float(row[column_index]) < float(value)]
    elif operator == "=":
        return [row for row in data[1:] if row[column_index] == value]
    else:
        raise ValueError(f"Unsupported operator '{operator}'")


parser = argparse.ArgumentParser(description="Чтение CSV файла")
parser.add_argument("file")
parser.add_argument("--where")

args = parser.parse_args()

text = read_csv(args.file)  # чтение csv файла
header = text[0] if text else []  # чтение заголовков
data = text[1:] if len(text) > 1 else []  # чтение остальных строк

if args.where:
    data = filter_csv(text, args.where)

print(tabulate(data, headers=header, tablefmt="grid"))
