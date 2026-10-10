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
