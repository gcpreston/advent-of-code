from typing import List, Iterable, Optional


def run(intcode: List[int], memory: int = 100,
        input_data: Iterable[int] = None,
        return_output: bool = False) -> Optional[List[int]]:
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
        8: 3,
        9: 1
    }

    pointer = 0  # position of current instruction being read
    base = 0  # relative base, day 9
    out = []  # only used if return_output is set to True
    if input_data:
        input_iter = iter(input_data)
        iter_finished = False
    else:
        input_iter = None
        iter_finished = True
    intcode += [0] * memory

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
            #   - mode 2: index specified by relative value of read parameter
            # INVARIANT: "Parameters that an instruction writes to will never
            #             be in immediate mode."
            position = pointer + i + 1
            if modes[i] == 0:
                params[i] = intcode[position]
            elif modes[i] == 1:
                params[i] = position
            elif modes[i] == 2:
                delta = intcode[pointer + i + 1]
                params[i] = intcode[base + delta]

        if opcode == 1:
            # add
            intcode[params[2]] = intcode[params[0]] + intcode[params[1]]
        elif opcode == 2:
            #  multiply
            intcode[params[2]] = intcode[params[0]] * intcode[params[1]]
        elif opcode == 3:
            # input
            # TODO: Clean up
            if not iter_finished:
                try:
                    intcode[params[0]] = next(input_iter)
                except StopIteration:
                    iter_finished = True
                    intcode[params[0]] = int(input('Input: '))
            else:
                intcode[params[0]] = int(input('Input: '))
        elif opcode == 4:
            # output
            if return_output:
                out.append(intcode[params[0]])
            else:
                print(intcode[params[0]])
        elif opcode == 5:
            # jump if true
            if intcode[params[0]]:
                pointer = intcode[params[1]]
                update = False
        elif opcode == 6:
            # jump if false
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
        elif opcode == 9:
            # adjust relative base
            base += intcode[params[0]]

        if update:
            pointer += np + 1

    if return_output:
        return out


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
