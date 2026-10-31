import unittest

from midpoint import above, below, both_sides, covers, equal_count, farthest, mean, median, nearest, none_hit, off_count, span, all_hit, some_hit


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
        self.assertTrue(covers([1, 4, 9], 5))
        self.assertFalse(covers([1, 4, 9], 0))
        self.assertEqual(below([1, 4, 9], 5), 2)
        self.assertEqual(above([1, 4, 9], 5), 1)
        self.assertEqual(equal_count([1, 5, 5, 9], 5), 2)
        self.assertTrue(both_sides([1, 4, 9], 5))
        self.assertFalse(both_sides([1, 4], 5))
        self.assertEqual(off_count([1, 5, 9], 5), 2)
        self.assertEqual(off_count([5, 5], 5), 0)
        self.assertTrue(none_hit([1, 9], 5))
        self.assertFalse(none_hit([1, 5], 5))


        self.assertTrue(all_hit([5, 5], 5))
        self.assertFalse(all_hit([1, 5], 5))

        self.assertTrue(some_hit([1, 5], 5))
        self.assertFalse(some_hit([1, 9], 5))

if __name__ == "__main__":
    unittest.main()
