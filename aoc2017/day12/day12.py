from itertools import chain


def connected(n: int, connections: dict) -> list:
    """Returns a list of programs that can communicate with n directly
    or indirectly.
    Advent of Code 2017, day 12, part 1."""
    visited = []
    queue = [n]
    while queue:
        current = queue.pop(0)
        new = [x for x in connections[current] if x not in visited]
        queue.extend(new)
        visited.extend(new)
    return visited


def get_groups(connections: dict) -> list:
    """Returns the groups within connections.
    Advent of Code 2017, day 12, part 2."""
    groups = []
    remaining = list(range(len(connections)))
    while remaining:
        n = remaining[0]
        groups.append(connected(n, connections))
        used = list(chain.from_iterable(groups))
        remaining = [x for x in remaining if x not in used]
    return groups


if __name__ == '__main__':
    contents = []
    with open('day12_input.txt') as file:
        for line in file.readlines():
            fixed_line = line.replace('<->', '').replace(',', '')
            contents.append([int(n) for n in fixed_line.split()])

    day12_input = {}
    for line in contents:
        day12_input[line[0]] = line[1:]

    print(len(connected(0, day12_input)))
    print(len(get_groups(day12_input)))
