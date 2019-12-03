import string
import networkx as nx

from aoc2017.day10.day10 import knot_hash


def hex_to_bin(h: string) -> string:
    """Converts hex to binary, keeping leading zeros."""
    b = ''
    for c in h:
        b += bin(int(c, 16))[2:].zfill(4)
    return b


def disk(s: string) -> list:
    """Generates the disk for the given string (using 0s and 1s instead of #s and .s)."""
    rows = []
    for i in range(128):
        h = hex_to_bin(knot_hash(f'{s}-{i}'))
        rows.append(list(h))
    return rows


def square_count(s: string) -> int:
    """Counts the number of squares in the disk for the given string.
    Advent of Code 2017, day 14, part 1."""
    d = disk(s)
    total = 0
    for r in d:
        total += sum(int(x) for x in r)
    return total


def region_count(s: string) -> int:
    """Counts the number of regions in the disk for the given string.
    Advent of Code 2017, day 14, part 2."""
    g = nx.Graph()
    d = disk(s)

    for row in range(len(d) - 1):
        for col in range(len(d[row]) - 1):
            current_node = f'{row},{col}'
            if d[row][col] == '1':
                g.add_node(current_node)
                test_node = f'{row + 1},{col}'
                if d[row + 1][col] == '1':
                    g.add_node(test_node)
                    g.add_edge(current_node, test_node)
                test_node = f'{row},{col + 1}'
                if d[row][col + 1] == '1':
                    g.add_node(test_node)
                    g.add_edge(current_node, test_node)

    return nx.number_connected_components(g)


def region_count_v2(s: string) -> int:
    """Counts the number of regions in the disk for the given string.
    Advent of Code 2017, day 14, part 2."""
    d = disk(s)
    seen = set()
    total = 0

    def dfs(row: int, col: int) -> None:
        """Discovers nodes within a region in d."""
        if (row, col) in seen:
            return
        if not d[row][col]:
            return
        seen.add((row, col))
        if row > 0:
            dfs(row - 1, col)
        if col > 0:
            dfs(row, col - 1)
        if row < 127:
            dfs(row + 1, col)
        if col < 127:
            dfs(row, col + 1)

    for row in range(128):
        for col in range(128):
            if (row, col) in seen:
                continue
            if d[row][col] == 0:
                continue
            total += 1
            dfs(row, col)
    return total


if __name__ == '__main__':
    day14_input = 'ffayrhll'
    print(square_count(day14_input))
    print(region_count(day14_input))
