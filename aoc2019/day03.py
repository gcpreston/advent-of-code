from typing import List, Set, Tuple

Wire = List[Tuple[str, int]]
Point = Tuple[int, int]


def points_touched(w: Wire) -> Set[Point]:
    """
    Calculate the set of points touched by wire w.
    """
    ret = set()
    cur = (0, 0)

    for direction, length in w:
        if direction == 'R':
            ret.update({(cur[0], cur[1] - o) for o in range(1, length + 1)})
            cur = (cur[0], cur[1] - length)
        elif direction == 'L':
            ret.update({(cur[0], cur[1] + o) for o in range(1, length + 1)})
            cur = (cur[0], cur[1] + length)
        elif direction == 'U':
            ret.update({(cur[0] + o, cur[1]) for o in range(1, length + 1)})
            cur = (cur[0] + length, cur[1])
        elif direction == 'D':
            ret.update({(cur[0] - o, cur[1]) for o in range(1, length + 1)})
            cur = (cur[0] - length, cur[1])

    return ret


def dist(w: Wire, p: Point) -> int:
    """
    Calculate distance to get to p from origin via w. Raises `RuntimeError`
    if p is not found on w.
    """
    total = 0
    cur = (0, 0)

    for direction, length in w:
        if direction == 'R':
            if cur[0] == p[0] and cur[1] - p[1] <= length:
                return total + (cur[1] - p[1])
            else:
                total += length
                cur = (cur[0], cur[1] - length)

        elif direction == 'L':
            if cur[0] == p[0] and p[1] - cur[1] <= length:
                return total + (p[1] - cur[1])
            else:
                total += length
                cur = (cur[0], cur[1] + length)

        elif direction == 'U':
            if cur[1] == p[1] and p[0] - cur[0] <= length:
                return total + (p[0] - cur[0])
            else:
                total += length
                cur = (cur[0] + length, cur[1])

        elif direction == 'D':
            if cur[1] == p[1] and cur[0] - p[0] <= length:
                return total + (cur[0] - p[0])
            else:
                total += length
                cur = (cur[0] - length, cur[1])

    raise RuntimeError('p not found on w')


def main(fn: str):
    with open(fn) as file:
        w1 = [(p[0], int(p[1:])) for p in file.readline().split(',')]
        w2 = [(p[0], int(p[1:])) for p in file.readline().split(',')]

    touched1 = points_touched(w1)
    touched2 = points_touched(w2)
    intersects = touched1.intersection(touched2)

    print('Part 1:', min([abs(i[0]) + abs(i[1]) for i in intersects]))
    print('Part 2:', min([dist(w1, i) + dist(w2, i) for i in intersects]))


if __name__ == '__main__':
    main('input/day03.txt')
