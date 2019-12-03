import unittest

from . import day03


class TestDay03(unittest.TestCase):

    def test_part1(self):
        claims = [(1, 3, 2, 5, 4)]
        self.assertEqual(0, day03.part1(claims))

        claims = [(1, 1, 3, 4, 4),
                  (1, 3, 1, 4, 4),
                  (1, 5, 5, 2, 2)]
        self.assertEqual(4, day03.part1(claims))


if __name__ == '__main__':
    unittest.main()
