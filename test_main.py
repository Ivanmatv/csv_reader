import pytest

from typing import List, Dict

from main import filter_csv, aggregate_csv


def test_filter_csv() -> None:
    """Тестирование функции фильтрации данных"""
    data: List[Dict[str, str]] = [
        {"name": "iphone 15 pro", "brand": "apple", "price": "999", "rating": "4.9"},
        {"name": "galaxy s23 ultra", "brand": "samsung", "price": "1199", "rating": "4.8"},
        {"name": "redmi note 12", "brand": "xiaomi", "price": "199", "rating": "4.6"},
    ]
    condition = "rating>4.7"
    filtered = filter_csv(data, condition)
    assert len(filtered) == 2
    assert filtered[0]['name'] == 'iphone 15 pro'
    assert filtered[1]['name'] == 'galaxy s23 ultra'


def test_aggregate_csv_avg() -> None:
    """Тестирование агрегации (среднее значение)"""
    data: List[Dict[str, str]] = [
        {"name": "iphone 15 pro", "brand": "apple", "price": "999", "rating": "4.9"},
        {"name": "galaxy s23 ultra", "brand": "samsung", "price": "1199", "rating": "4.8"},
        {"name": "redmi note 12", "brand": "xiaomi", "price": "199", "rating": "4.6"},
    ]
    condition = "rating=avg"
    result = aggregate_csv(data, condition)
    expected_avg = (4.9 + 4.8 + 4.6) / 3
    assert result == pytest.approx(expected_avg)  # Используем approx для сравнения float


def test_aggregate_csv_min() -> None:
    """Тестирование агрегации (минимальное значение)"""
    data: List[Dict[str, str]] = [
        {"name": "iphone 15 pro", "brand": "apple", "price": "999", "rating": "4.9"},
        {"name": "galaxy s23 ultra", "brand": "samsung", "price": "1199", "rating": "4.8"},
        {"name": "redmi note 12", "brand": "xiaomi", "price": "199", "rating": "4.6"},
    ]
    condition = "rating=min"
    result = aggregate_csv(data, condition)
    assert result == 4.6


def test_aggregate_csv_max() -> None:
    """Тестирование агрегации (максимальное значение)"""
    data: List[Dict[str, str]] = [
        {"name": "iphone 15 pro", "brand": "apple", "price": "999", "rating": "4.9"},
        {"name": "galaxy s23 ultra", "brand": "samsung", "price": "1199", "rating": "4.8"},
        {"name": "redmi note 12", "brand": "xiaomi", "price": "199", "rating": "4.6"},
    ]
    condition = "rating=max"
    result = aggregate_csv(data, condition)
    assert result == 4.9
