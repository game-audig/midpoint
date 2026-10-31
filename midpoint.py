"""Median of a list of numbers."""
from __future__ import annotations


def median(values: list[float]) -> float:
    if not values:
        raise ValueError("空列表没有中位数")
    ordered = sorted(values)
    mid = len(ordered) // 2
    if len(ordered) % 2:
        return float(ordered[mid])
    return (ordered[mid - 1] + ordered[mid]) / 2


def mean(values: list[float]) -> float:
    if not values:
        raise ValueError("空列表没有平均数")
    return sum(values) / len(values)


def span(values: list[float]) -> float:
    if not values:
        raise ValueError("空列表没有跨度")
    return max(values) - min(values)


def nearest(values: list[float], target: float) -> float:
    if not values:
        raise ValueError("空列表没有最近值")
    return min(values, key=lambda value: (abs(value - target), value))


def farthest(values: list[float], target: float) -> float:
    if not values:
        raise ValueError("空列表没有最远值")
    return max(values, key=lambda value: (abs(value - target), value))


def covers(values: list[float], target: float) -> bool:
    if not values:
        raise ValueError("空列表没有跨度")
    return min(values) <= target <= max(values)


def below(values: list[float], target: float) -> int:
    return sum(1 for value in values if value < target)


def above(values: list[float], target: float) -> int:
    return sum(1 for value in values if value > target)


def equal_count(values: list[float], target: float) -> int:
    return sum(1 for value in values if value == target)


def both_sides(values: list[float], target: float) -> bool:
    return below(values, target) > 0 and above(values, target) > 0


def off_count(values: list[float], target: float) -> int:
    return below(values, target) + above(values, target)


def none_hit(values: list[float], target: float) -> bool:
    return bool(values) and off_count(values, target) == len(values)

def all_hit(values: list[float], target: float) -> bool:
    return bool(values) and off_count(values, target) == 0

def some_hit(values: list[float], target: float) -> bool:
    return equal_count(values, target) > 0
