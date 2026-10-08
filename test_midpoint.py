import unittest

from midpoint import farthest, mean, median, nearest, span


class MidpointTest(unittest.TestCase):
    def test_odd_and_even(self) -> None:
        self.assertEqual(median([3, 1, 2]), 2)
        self.assertEqual(median([1, 2, 3, 4]), 2.5)
        self.assertEqual(span([1, 4, 2]), 3)
        self.assertEqual(mean([1, 2, 3]), 2)
        with self.assertRaises(ValueError):
            mean([])
        with self.assertRaises(ValueError):
            median([])
        self.assertEqual(nearest([1, 4, 9], 5), 4)
        self.assertEqual(farthest([1, 4, 9], 5), 9)
        with self.assertRaises(ValueError):
            nearest([], 1)


if __name__ == "__main__":
    unittest.main()
