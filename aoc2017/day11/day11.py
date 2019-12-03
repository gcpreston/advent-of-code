import string


def steps_away(directions: list) -> int:
    """Calculates the number of steps required to reach the child process after it
    took the steps described in directions.
    Advent of Code 2017, day 11, part 1."""
    steps = {'nw': 0, 'n': 0, 'ne': 0, 'sw': 0, 's': 0, 'se': 0}
    for d in directions:
        steps[d] += 1
    steps = cancel_steps(steps)
    steps = convert_steps(steps)

    total = 0
    for v in steps.values():
        total += v
    return total


def cancel_steps(steps: dict) -> dict:
    """If two steps cancel each other out, removes them."""

    def cancel(dir1: string, dir2: string) -> dict:
        """n + s,
        nw + se,
        ne + sw"""
        if steps[dir1] > steps[dir2]:
            steps[dir1] -= steps[dir2]
            steps[dir2] = 0
        else:
            steps[dir2] -= steps[dir1]
            steps[dir1] = 0
        return steps

    steps = cancel('n', 's')
    steps = cancel('nw', 'se')
    steps = cancel('ne', 'sw')
    return steps


def convert_steps(steps: dict) -> dict:
    """If two steps together can be simplified to a single one, does so."""

    def convert(dir1: string, dir2: string, result: string) -> dict:
        """nw + ne = n,
        sw + se = s,
        nw + s = sw,
        ne + s = se,
        sw + n = nw,
        se + n = ne
        '"""
        if steps[dir1] > steps[dir2]:
            steps[result] += steps[dir2]
            steps[dir1] -= steps[dir2]
            steps[dir2] = 0
        else:
            steps[result] += steps[dir1]
            steps[dir2] -= steps[dir1]
            steps[dir1] = 0
        return steps

    steps = convert('nw', 'ne', 'n')
    steps = convert('sw', 'se', 's')
    steps = convert('nw', 's', 'sw')
    steps = convert('ne', 's', 's')
    steps = convert('sw', 'n', 'nw')
    steps = convert('se', 'n', 'ne')
    return steps


def max_steps_away(directions: list) -> int:
    """Calculates how many steps away the furthest the child process ever got was.
    Advent of Code 2017, day 11, part 2."""
    max_distance = 0
    for i in range(len(directions)):
        distance = steps_away(directions[:i])
        if distance > max_distance:
            max_distance = distance
    return max_distance


if __name__ == '__main__':
    with open('day11_input.txt') as file:
        day11_input = file.read().strip().split(',')

    print(steps_away(day11_input))
    print(max_steps_away(day11_input))
