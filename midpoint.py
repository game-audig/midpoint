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
