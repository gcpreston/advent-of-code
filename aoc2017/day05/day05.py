def steps_to_exit_v1(jumps: list) -> int:
    """Calculates the number of steps needed to reach the exit of the jump offset list.
    Advent of Code 2017, day 5, part 1."""
    local_jumps = list(jumps)
    steps = 0
    i = 0
    j = 0
    while j < len(local_jumps):
        j = i + local_jumps[i]
        local_jumps[i] += 1
        i = j
        steps += 1
    return steps


def steps_to_exit_v2(jumps: list) -> int:
    """Calculates the number of steps needed to reach the exit of the jump offset list.
    Advent of Code 2017, day 5, part 1."""
    local_jumps = list(jumps)
    steps = 0
    i = 0
    j = 0
    while j < len(local_jumps):
        j = i + local_jumps[i]
        if local_jumps[i] >= 3:
            local_jumps[i] -= 1
        else:
            local_jumps[i] += 1
        i = j
        steps += 1
    return steps


if __name__ == '__main__':
    with open('day05_input.txt') as file:
        day05_input = [int(n) for n in file.readlines()]

    print(steps_to_exit_v1(day05_input))
    print(steps_to_exit_v2(day05_input))
