import unittest

from midpoint import median, span


class MidpointTest(unittest.TestCase):
    def test_odd_and_even(self) -> None:
        self.assertEqual(median([3, 1, 2]), 2)
        self.assertEqual(median([1, 2, 3, 4]), 2.5)
        self.assertEqual(span([1, 4, 2]), 3)
        with self.assertRaises(ValueError):
            median([])


if __name__ == "__main__":
    unittest.main()
