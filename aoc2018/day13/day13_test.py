import unittest

from . import day13


class TestDay13(unittest.TestCase):

    def test_firstcrash(self):
        with open('test_input.txt') as file:
            test_initial = [line.strip() for line in file.readlines()]

        self.assertEqual((7, 3), day13.firstcrash(test_initial))
