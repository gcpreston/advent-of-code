from typing import List


def run(intcode: List[int]) -> None:
    """
    Run an Intcode program. Modifies the given list.
    """
    # opcode -> number of params
    num_params = {
        99: 0,
        1: 3,
        2: 3,
        3: 1,
        4: 1,
        5: 2,
        6: 2,
        7: 3,
        8: 3
    }

    pointer = 0  # position of current instruction being read

    while intcode[pointer] != 99:
        instr: str = str(intcode[pointer])
        opcode: int = int(instr[-2:])
        np = num_params[opcode]
        modes: List[int] = [int(i) for i in instr[-3::-1]]
        modes += [0] * (np - len(modes))  # pad to length np
        update = True  # whether to increment the instruction pointer at end

        params: List[int] = [0] * np
        for i in range(np):
            # Parameter values will always be accessed using intcode[params[i]].
            # As such, params[i] will contain:
            #   - mode 0: index specified by value of read parameter
            #   - mode 1: index of read parameter (so intcode[params[i]] gives
            #             the raw value)
            # INVARIANT: "Parameters that an instruction writes to will never
            #             be in immediate mode."
            if modes[i] == 0:
                params[i] = intcode[pointer + i + 1]
            else:
                params[i] = pointer + i + 1

        if opcode == 1:
            # add
            intcode[params[2]] = intcode[params[0]] + intcode[params[1]]
        elif opcode == 2:
            #  multiply
            intcode[params[2]] = intcode[params[0]] * intcode[params[1]]
        elif opcode == 3:
            # input
            intcode[params[0]] = int(input('Input: '))
        elif opcode == 4:
            # output
            print(intcode[params[0]])
        elif opcode == 5:
            # jump-if-true
            if intcode[params[0]]:
                pointer = intcode[params[1]]
                update = False
        elif opcode == 6:
            # jump-if-false
            if not intcode[params[0]]:
                pointer = intcode[params[1]]
                update = False
        elif opcode == 7:
            # less than
            if intcode[params[0]] < intcode[params[1]]:
                intcode[params[2]] = 1
            else:
                intcode[params[2]] = 0
        elif opcode == 8:
            # equals
            if intcode[params[0]] == intcode[params[1]]:
                intcode[params[2]] = 1
            else:
                intcode[params[2]] = 0

        if update:
            pointer += np + 1


def main(fn: str):
    with open(fn) as file:
        ic_original: List[int] = [int(n) for n in file.read().split(',')]

    intcode = ic_original.copy()
    intcode[1] = 12
    intcode[2] = 2
    run(intcode)

    print('Part 1:', intcode[0])

    for noun in range(100):
        for verb in range(100):
            ic_copy = ic_original.copy()
            ic_copy[1] = noun
            ic_copy[2] = verb
            run(ic_copy)

            if ic_copy[0] == 19690720:
                print('Part 2:', 100 * noun + verb)
                return


if __name__ == '__main__':
    main('input/day02.txt')
