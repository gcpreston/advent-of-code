from aoc2019.day02 import run


def main(fn: str):
    with open(fn) as file:
        program = [int(i) for i in file.read().strip().split(',')]

    run(program, memory=10, input_data=[1])


if __name__ == '__main__':
    main('input/day09_test1.txt')
