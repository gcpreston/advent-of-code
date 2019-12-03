import math


def fuel(mass: int) -> int:
    """
    Get the fuel required to launch a module given its mass.
    """
    return math.floor(mass / 3) - 2


def total_fuel(mass: int) -> int:
    """
    Get the total fuel required, including the fuel for the extra fuel.
    """
    total = 0
    extra = fuel(mass)

    while extra > 0:
        total += extra
        extra = fuel(extra)

    return total


def main(fn: str):
    with open(fn) as file:
        masses = [int(m) for m in file.readlines()]

    print('Part 1:', sum([fuel(m) for m in masses]))
    print('Part 2:', sum([total_fuel(m) for m in masses]))


if __name__ == '__main__':
    main('input/day01.txt')
