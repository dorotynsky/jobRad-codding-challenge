import unittest

from src.merge_intervals import merge_intervals


class TestMergeIntervals(unittest.TestCase):
    def test_no_intervals(self):
        # No intervals
        self.assertEqual(merge_intervals([]), [])

    def test_single_interval(self):
        # Only one interval
        self.assertEqual(merge_intervals([(5, 10)]), [(5, 10)])

    def test_non_overlapping_intervals(self):
        # Intervals that do not overlap
        self.assertEqual(merge_intervals([(1, 3), (5, 7), (8, 10)]), [(1, 3), (5, 7), (8, 10)])

    def test_overlapping_intervals(self):
        # Overlapping intervals
        self.assertEqual(merge_intervals([(1, 5), (2, 6), (8, 10), (9, 12)]), [(1, 6), (8, 12)])


if __name__ == "__main__":
    unittest.main()
