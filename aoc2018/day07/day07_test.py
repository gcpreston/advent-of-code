import unittest

from al60.data.graphs import DirectedGraph
from . import day07


class TestDay07(unittest.TestCase):

    def test_part2(self):
        g = DirectedGraph()
        g.add_nodes('A', 'B', 'C', 'D', 'E', 'F')

        g.add_edge('C', 'A')
        g.add_edge('C', 'F')
        g.add_edge('A', 'B')
        g.add_edge('A', 'D')
        g.add_edge('B', 'E')
        g.add_edge('D', 'E')
        g.add_edge('F', 'E')

        self.assertEqual(258, day07.part2(g, n=2))
