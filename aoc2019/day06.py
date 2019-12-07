import networkx as nx


def count_orbits(g: nx.DiGraph) -> int:
    """
    Count the total number of orbits in a graph.
    """
    return sum([len(nx.ancestors(g, n)) for n in g.nodes])


def main(fn: str):
    g1 = nx.DiGraph()

    with open(fn) as file:
        for line in file.readlines():
            u, v = line.strip().split(')')
            g1.add_node(u)
            g1.add_node(v)
            g1.add_edge(u, v)

    print('Part 1:', count_orbits(g1))
    g2 = nx.Graph(g1)  # convert to undirected graph for part 2
    print('Part 2:', len(nx.shortest_path(g2, 'YOU', 'SAN')) - 3)


if __name__ == '__main__':
    main('input/day06.txt')
