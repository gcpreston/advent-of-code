def main():
    with open('input.txt') as file:
        initial_state = file.readline().strip()[15:]
        notes = {line.strip().split(' => ')[0] for line in file.readlines()[1:]
                 if line[-2] == '#'}

    print('Part 1:', generation(20, initial_state, notes))

    # change should be constant after 500 generations
    gen_499 = generation(499, initial_state, notes)
    gen_500 = generation(500, initial_state, notes)

    print('Part 2:', gen_500 + ((gen_500 - gen_499) * (50000000000 - 500)))


def generation(n, initial_state, notes):
    # a state is a set of pot numbers whuch contain a plant
    current = {idx for idx, val in enumerate(initial_state) if val == '#'}

    for i in range(n):
        # print(f'{i}: ({sum(current)}) {state_str(current)}')

        new = set()
        for pot in range(min(current) - 2, max(current) + 3):
            if plant(pot, current, notes):
                new.add(pot)

        current = new

    return sum(current)


def plant(pot, state, notes) -> bool:
    n = note(pot, state)

    if n in notes:
        return True
    else:
        return False


def note(pot, state):
    s = ''
    for p in range(pot - 2, pot + 3):
        if p in state:
            s += '#'
        else:
            s += '.'

    return s


def state_str(state):
    s = ''
    for p in range(min(state), max(state) + 1):
        if p in state:
            s += '#'
        else:
            s += '.'

    return s


if __name__ == '__main__':
    main()
