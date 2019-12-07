from aoc2019.day02 import run


def main(fn: str):
    with open(fn) as file:
        intcode = [int(n) for n in file.read().split(',')]
    run(intcode)


if __name__ == '__main__':
    main('input/day05.txt')
