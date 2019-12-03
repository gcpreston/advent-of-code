import unittest

from . import day08


class TestDay08(unittest.TestCase):

    def test_part1(self):
        nums = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]
        self.assertEqual(138, day08.part1(nums))
