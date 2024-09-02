import unittest

from src.merge_intervals import merge_intervals, read_intervals_from_file, use_default_intervals
import os
import tempfile


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

    def test_touching_intervals(self):
        # Test case with intervals that touch but do not overlap
        self.assertEqual(merge_intervals([(1, 3), (3, 5), (5, 7)]), [(1, 7)])

    def test_nested_intervals(self):
        # Test case with nested intervals (one inside the other)
        self.assertEqual(merge_intervals([(1, 10), (2, 5), (6, 9)]), [(1, 10)])

    def test_mixed_intervals(self):
        # Test case with a mix of overlapping and non-overlapping intervals
        self.assertEqual(merge_intervals([(1, 4), (2, 6), (8, 10), (15, 18)]), [(1, 6), (8, 10), (15, 18)])

    def test_unsorted_intervals(self):
        # Test case with unsorted intervals
        self.assertEqual(merge_intervals([(8, 10), (1, 3), (2, 6), (15, 18)]), [(1, 6), (8, 10), (15, 18)])

    def test_overlapping_and_touching(self):
        # Test case with a combination of overlapping and touching intervals
        self.assertEqual(merge_intervals([(1, 3), (2, 6), (6, 8), (9, 12)]), [(1, 8), (9, 12)])

    def test_use_default_intervals(self):
        expected = [(2, 23), (25, 30)]
        result = merge_intervals(use_default_intervals())
        self.assertEqual(result, expected)

    def test_read_intervals_from_file(self):
        # create temp file with intervals
        temp = tempfile.NamedTemporaryFile(delete=False)
        temp.write(b"1,3\n4,6\n7,9")
        temp.close()

        expected = [(1, 3), (4, 6), (7, 9)]
        result = read_intervals_from_file(temp.name)

        # delete temporary file
        os.unlink(temp.name)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
