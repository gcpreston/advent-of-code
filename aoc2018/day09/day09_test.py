import unittest

from . import day09


class TestDay09(unittest.TestCase):

    def test_solve(self):
        self.assertEqual(32, day09.solve(9, 25))
        self.assertEqual(8317, day09.solve(10, 1618))
        self.assertEqual(146373, day09.solve(13, 7999))
        self.assertEqual(2764, day09.solve(17, 1104))
        self.assertEqual(54718, day09.solve(21, 6111))
        self.assertEqual(37305, day09.solve(30, 5807))
