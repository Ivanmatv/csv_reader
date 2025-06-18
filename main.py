import csv
import argparse


def read_csv(file_path):
    """Чтение CSV файла."""
    with open(file_path, newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        return [row for row in reader]


parser = argparse.ArgumentParser(description="Чтение CSV файла")
parser.add_argument("file")
args = parser.parse_args()

rows = read_csv(args.file)

print(rows)
