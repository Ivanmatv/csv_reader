import csv
import argparse

from tabulate import tabulate


def read_csv(file_path):
    """Чтение CSV файла."""
    with open(file_path, newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        return [row for row in reader]


parser = argparse.ArgumentParser(description="Чтение CSV файла")
parser.add_argument("file")
args = parser.parse_args()

text = read_csv(args.file)

header = text[0] if text else []  # чтение заголовков
data = text[1:] if len(text) > 1 else []  # чтение остальных строк

print(tabulate(data, headers=header))
