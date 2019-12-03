def largest_register(instructions: list) -> int:
    """Returns the largest value in any register after completing the instructions.
    Advent of Code 2017, day 8, part 1."""
    registers = {}
    for line in instructions:
        try:
            registers[line[4]]
        except KeyError:
            registers[line[4]] = 0
        try:
            registers[line[0]]
        except KeyError:
            registers[line[0]] = 0

        if eval(f"registers['{line[4]}'] {line[5]} {line[6]}"):
            if line[1] == 'inc':
                registers[line[0]] += int(line[2])
            else:
                registers[line[0]] -= int(line[2])

    return max(registers.values())


def register_max(instructions: list) -> int:
    """Returns the largest value in any register at any point while evaluating instructions.
    Advent of Code 2017, day 8, part 2."""
    max_value = 0
    registers = {}
    for line in instructions:
        try:
            registers[line[4]]
        except KeyError:
            registers[line[4]] = 0
        try:
            registers[line[0]]
        except KeyError:
            registers[line[0]] = 0

        if eval(f"registers['{line[4]}'] {line[5]} {line[6]}"):
            if line[1] == 'inc':
                registers[line[0]] += int(line[2])
            else:
                registers[line[0]] -= int(line[2])

        if max(registers.values()) > max_value:
            max_value = max(registers.values())

    return max_value


if __name__ == '__main__':
    with open('day08_input.txt') as file:
        day08_input = [line.split() for line in file.readlines()]

    print(largest_register(day08_input))
    print(register_max(day08_input))
