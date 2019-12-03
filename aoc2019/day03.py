from typing import List, Set, Tuple, Dict

Wire = List[Tuple[str, int]]
Point = Tuple[int, int]

d: Dict[str, Point] = {'L': (1, 0), 'R': (-1, 0), 'U': (0, 1), 'D': (0, -1)}


def point_add(p1: Point, p2: Point) -> Point:
    return tuple(map(sum, zip(p1, p2)))


def points_touched(w: Wire) -> Set[Point]:
    """
    Calculate the set of points touched by wire w.
    """
    ret = set()
    cur = (0, 0)

    for direction, length in w:
        for i in range(length):
            cur = point_add(cur, d[direction])
            ret.add(cur)

    return ret


def dist(w: Wire, p: Point) -> int:
    """
    Calculate distance to get to p from origin via w. Raises `RuntimeError`
    if p is not found on w.
    """
    total = 0
    cur = (0, 0)

    for direction, length in w:
        for i in range(length):
            total += 1

            if (cur := point_add(cur, d[direction])) == p:
                return total

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
