from typing import List


def run(intcode: List[int]) -> List[int]:
    """
    Run an Intcode program. Makes a copy of the input list, which is returned
    at the end.
    """
    new_intcode = intcode.copy()

    # position of current opcode being read
    i = 0

    while new_intcode[i] != 99:
        a = new_intcode[new_intcode[i + 1]]
        b = new_intcode[new_intcode[i + 2]]

        if new_intcode[i] == 1:
            # add
            new_intcode[new_intcode[i + 3]] = a + b
        elif new_intcode[i] == 2:
            #  multiply
            new_intcode[new_intcode[i + 3]] = a * b

        i += 4

    return new_intcode


def main(fn: str):
    with open(fn) as file:
        intcode: List[int] = [int(n) for n in file.read().split(',')]

    intcode[1] = 12
    intcode[2] = 2
    part1_intcode = run(intcode)

    print('Part 1:', part1_intcode[0])

    for noun in range(100):
        for verb in range(100):
            intcode[1] = noun
            intcode[2] = verb
            part2_intcode = run(intcode)

            if part2_intcode[0] == 19690720:
                print('Part 2:', 100 * noun + verb)
                return


if __name__ == '__main__':
    main('input/day02.txt')
