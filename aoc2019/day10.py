import math

from typing import Tuple, List, Dict
from collections import defaultdict


def calc_base(asteroid: Tuple[int, int], monitor: Tuple[int, int]) \
        -> Tuple[int, int]:
    """
    Find the smallest (dy, dx) such that
    ``monitor`` + ((dy, dx) * ``n``) = ``asteroid`` for some ``n``.
    """
    if asteroid == monitor:
        return 0, 0

    dy = asteroid[0] - monitor[0]
    dx = asteroid[1] - monitor[1]
    div = math.gcd(dy, dx)

    dy //= div  # will not round, just casts float to int
    dx //= div

    return dy, dx


def visible(asteroid: Tuple[int, int], monitor: Tuple[int, int],
            data: List[str]) -> bool:
    """
    Is ``asteroid`` visible from ``monitor``?
    """
    dy, dx = calc_base(asteroid, monitor)

    cur: Tuple[int, int] = monitor
    while cur != asteroid:
        cur = (cur[0] + dy, cur[1] + dx)

        if cur == asteroid or \
                cur[0] < 0 or cur[1] < 0 or \
                cur[0] >= len(data) or cur[1] >= len(data[0]):
            return True
        elif data[cur[0]][cur[1]] == '#':
            return False


def count_visible(monitor: Tuple[int, int], data: List[str]) -> int:
    if data[monitor[0]][monitor[1]] != '#':
        return 0

    count = 0
    for r in range(len(data)):
        for c in range(len(data[0])):
            if data[r][c] == '#' and visible((r, c), monitor, data):
                count += 1
    return count


def map_asteroids(monitor: Tuple[int, int], data: List[str]) \
        -> Dict[Tuple[int, int], List[Tuple[int, int]]]:
    """
    Sort asteroids into groups of lines. The returned dict works as follows:
    Each key is the line on which asteroids fall. This means if you drew a
    line from ``monitor`` in the direction of a key and kept going, you
    would hit each of the asteroids in the associated list, in order.

    TODO: It would probably be easier to make the return value its own class,
          so iterating over it later is easier
    """
    ret: Dict[Tuple[int, int], List[Tuple[int, int]]] = defaultdict(list)

    for r in range(len(data)):
        for c in range(len(data[r])):

            if data[r][c] == '#':
                base = calc_base((r, c), monitor)

                if base != (0, 0):
                    ret[base].append((r, c))
    return ret


def base_key(base: Tuple[int, int]) -> float:
    """
    Key for sorting bases by radians away from vertical, clockwise.
    - (+dy, 0) -> 0.0
    - (0, +dx) -> pi / 2
    - (-dy, 0) -> pi
    - (0, -dx) -> 3 * pi / 2
    """
    dy, dx = base
    t = math.atan2(-dy, dx)  # for us, +dy means go down, so negate dy

    if math.pi / 2 < t <= math.pi:
        # Quadrant 2 weird case
        # For every other quadrant, (math.pi / 2) - t works
        # Returns from interval [(4/3) * math.pi, 2 * math.pi]
        return (2 * math.pi) - math.fabs((math.pi / 2) - t)
    else:
        return (math.pi / 2) - t


def main(fn: str):
    with open(fn) as file:
        contents = [line.strip() for line in file.readlines()]

    max_count = 0
    max_p = None

    for r in range(len(contents)):
        for c in range(len(contents[r])):
            if (count := count_visible((r, c), contents)) > max_count:
                max_count = count
                max_p = (r, c)

    print('Part 1:', max_count, max_p)

    # Part 2: IDEA
    # 1. Parse asteroids into (dy, dx) -> [asteroids...]
    # 2. Sort keys by (1) arctan(dy/dx) (2) signs, i.e. (3, -2) would come
    #    before (-3, 2) when going clockwise. Also check for vertical angles
    #    by checking for (x, 0).
    # 3. Iterate over keys circularly and pop from left of corresponding list.
    # 4. Do this 200 times.

    m = map_asteroids(max_p, contents)
    order = sorted(m.keys(), key=lambda a: base_key(a))

    i = 0
    count = 0
    last_destroyed = None
    while count < 200:
        found = False
        while not found:
            if not m:
                print('Less than 200 asteroids found.')
                exit(0)

            # check if asteroid list is non-empty
            if ast := m[order[i % len(order)]]:
                found = True
                last_destroyed = ast.pop(0)
                count += 1
            else:
                del m[order[i % len(order)]]
            i += 1

    print('Part 2:', (last_destroyed[1] * 100) + last_destroyed[0])


if __name__ == '__main__':
    main('input/day10_test1.txt')
