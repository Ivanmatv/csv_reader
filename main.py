import argparse
import csv
import re

from tabulate import tabulate
from typing import List, Dict, Union, Optional, Any


def read_csv(file_path: str) -> List[Dict[str, str]]:
    """Чтение CSV файла."""
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        data = list(reader)
    return data


def filter_csv(data: List[Dict[str, str]], condition: str) -> List[Dict[str, str]]:
    """Фильтрация данных по условию."""
    match = re.match(r"(\w+)\s*(>=|<=|<|>|=)\s*(\S+)", condition)
    if not match:
        print("Invalid filter condition")
        return []

    column, operator, value = match.groups()

    try:                            # Обрабатываем строки
        value = float(value)
        is_numeric = True
    except ValueError:
        value = value.strip()
        is_numeric = False

    if is_numeric:
        if operator == '>':
            return [row for row in data if float(row[column]) > value]
        elif operator == '<':
            return [row for row in data if float(row[column]) < value]
        elif operator == '=':
            return [row for row in data if float(row[column]) == value]
        elif operator == '>=':
            return [row for row in data if float(row[column]) >= value]
        elif operator == '<=':
            return [row for row in data if float(row[column]) <= value]
    else:
        if operator == '=':
            return [row for row in data if row[column] == value]

    return []


def aggregate_csv(data: List[Dict[str, str]], aggregate_condition: str) -> Optional[float]:
    """Агригирование данных по условиям."""
    column, aggregation_type = aggregate_condition.split('=')
    column = column.strip()
    aggregation_type = aggregation_type.strip()
    values = [float(row['rating']) for row in data]

    if aggregation_type == 'avg':
        return sum(values) / len(values)
    elif aggregation_type == 'min':
        return min(values)
    elif aggregation_type == 'max':
        return max(values)
    return None


def main() -> None:
    """Основная функция."""
    parser = argparse.ArgumentParser(description="Чтение CSV файла")
    parser.add_argument('--file', type=str, required=True)
    parser.add_argument('--where', type=str)
    parser.add_argument('--aggregate', type=str)

    args = parser.parse_args()

    data = read_csv(args.file)

    if args.where:
        data = filter_csv(data, args.where)

    if args.aggregate:
        result = aggregate_csv(data, args.aggregate)
        aggregation_type = args.aggregate.split('=')[1].strip()
        table = [[aggregation_type], [result]]
        print(tabulate(table, tablefmt='grid', stralign='center'))
        return

    headers = data[0].keys() if data else []
    table = [row.values() for row in data]
    print(tabulate(table, headers=headers, tablefmt='grid'))


if __name__ == "__main__":
    main()
