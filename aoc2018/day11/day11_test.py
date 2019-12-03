import unittest

from . import day11


class TestDay11(unittest.TestCase):

    def test_power_level(self):
        self.assertEqual(4, day11.powerlevel(3, 5, 8))
        self.assertEqual(-5, day11.powerlevel(122, 79, 57))
        self.assertEqual(0, day11.powerlevel(217, 196, 39))
        self.assertEqual(4, day11.powerlevel(101, 153, 71))

    def test_squaresum(self):
        grid = day11.gengrid(300, 300, 18)

        self.assertEqual((33, 45), day11.maxsquare(300, 300, 18))
