import unittest

from . import day01


class TestDay01(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(3, day01.part1([+1, -2, +3, +1]))
        self.assertEqual(3, day01.part1([+1, +1, +1]))
        self.assertEqual(0, day01.part1([+1, +1, -2]))
        self.assertEqual(-6, day01.part1([-1, -2, -3]))

    def test_part2(self):
        self.assertEqual(0, day01.part2([+1, -1]))
        self.assertEqual(10, day01.part2([+3, +3, +4, -2, -4]))
        self.assertEqual(5, day01.part2([-6, +3, +8, +5, -6]))
        self.assertEqual(14, day01.part2([+7, +7, -2, -7, -4]))


if __name__ == '__main__':
    unittest.main()
