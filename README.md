# midpoint

Median of a list. An even count averages the two middle values. The input list is not sorted in place.

```python
from midpoint import median, span, mean, nearest, farthest, covers, below, above, equal_count, both_sides, off_count, none_hit, all_hit

median([3, 1, 2])  # 2
span([1, 4, 2])    # 3
mean([1, 2, 3])    # 2
```

```bash
python -m unittest test_midpoint.py
```

MIT
