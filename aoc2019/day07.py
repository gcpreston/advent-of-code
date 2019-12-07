from itertools import permutations
from typing import List

from aoc2019.day02 import run


def to_base(n: int, b: int) -> str:
    bs = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return '0' if not n else to_base(n//b, b).lstrip("0") + bs[n % b]


def max_signal(intcode: List[int], settings: List[int]) -> int:
    biggest = 0
    for p in permutations(settings):
        prog = intcode.copy()
        seq = iter(p)
        signal = 0

        for _ in range(5):
            out = run(prog,
                      input_data=[next(seq), signal],
                      return_output=True)
            signal = out[0]

        if signal > biggest:
            biggest = signal
    return biggest


def max_signal_loop(intcode: List[int], settings: List[int]) -> int:
    pass


def main(fn: str):
    with open(fn) as file:
        intcode = [int(n) for n in file.read().split(',')]

    print('Part 1:', max_signal(intcode, [0, 1, 2, 3, 4]))
    print('Part 2:', max_signal_loop(intcode, [5, 6, 7, 8, 9]))


if __name__ == '__main__':
    main('input/day07.txt')
