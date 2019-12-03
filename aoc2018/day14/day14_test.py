import unittest

from . import day14


class TestDay14(unittest.TestCase):

    def test_part1(self):
        self.assertEqual('5158916779', day14.part1(9))
        self.assertEqual('0124515891', day14.part1(5))
        self.assertEqual('9251071085', day14.part1(18))
        self.assertEqual('5941429882', day14.part1(2018))

    def test_part2(self):
        self.assertEqual(9, day14.part2('51589'))
        self.assertEqual(5, day14.part2('01245'))
        self.assertEqual(18, day14.part2('92510'))
        self.assertEqual(2018, day14.part2('59414'))
