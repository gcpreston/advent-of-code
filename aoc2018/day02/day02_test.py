import unittest

from . import day02


class TestDay01(unittest.TestCase):

    def test_part1(self):
        boxes = ['abcdef',
                 'bababc',
                 'abbcde',
                 'abcccd',
                 'aabcdd',
                 'abcdee',
                 'ababab']
        self.assertEqual(12, day02.part1(boxes))

    def test_part2(self):
        boxes = ['abcde',
                 'fghij',
                 'klmno',
                 'pqrst',
                 'fguij',
                 'axcye',
                 'wvxyz']
        self.assertEqual('fgij', day02.part2(boxes))


if __name__ == '__main__':
    unittest.main()
