# TODO: change the scope so tower doesn't have to be passed to every function
import string


class Program:

    def __init__(self, info: string):
        info = info.replace(',', '').split()

        self.name = info[0]
        self.weight = int(info[1][1:-1])
        self.children = info[3:]


def parent(name: string, tower: list) -> string:
    """Finds the parent of the given program."""
    for program in tower:
        if name in program.children:
            return program


def bottom(tower: list) -> string:
    """Finds the bottom program in the tower.
    Advent of Code 2017, day 7, part 1."""
    current = tower[0]
    current_parent = parent(current.name, tower)
    while current_parent:
        current = current_parent
        current_parent = parent(current.name, tower)
    return current.name


def get_program(name: string, tower: list) -> Program:
    """Returns the Program within tower with the given name."""
    for p in tower:
        if p.name == name:
            return p


def total_weight(p: Program, tower: list) -> int:
    """Calculates the sum of the weights of p and all the programs above it."""
    if not p.children:
        return p.weight

    child_programs = [get_program(s, tower) for s in p.children]
    child_weight = sum(total_weight(c, tower) for c in child_programs)
    return p.weight + child_weight


def child_weights(p: Program, tower: list) -> list:
    """Returns the weights of p.children."""
    weights = []
    for c in p.children:
        weights.append(total_weight(get_program(c, tower), tower))
    return weights


def get_unbalanced(p: Program, tower: list) -> Program:
    """Returns the origin of the sub-tower that's unbalanced."""

    def frequencies(lst: list) -> dict:
        """Returns a dict with the frequencies of every element in lst."""
        d = {}
        for e in lst:
            try:
                d[e] += 1
            except KeyError:
                d[e] = 1
        return d

    weights = child_weights(p, tower)
    weight_freqs = frequencies(weights)
    if len(set(weight_freqs.values())) == 1:
        return None

    unique_val = min(weight_freqs, key=weight_freqs.get)
    unique_index = weights.index(unique_val)
    unique_name = p.children[unique_index]

    return get_program(unique_name, tower)


def corrected_weight(tower: list) -> int:
    """Given that exactly one program within tower has an incorrect weight, returns what its weight
    would need to be to balance the tower.
    Advent of Code 2017, day 7, part 2."""
    origin = get_program(bottom(tower), tower)
    unbalanced = get_unbalanced(origin, tower)

    while get_unbalanced(unbalanced, tower):
        origin = unbalanced
        unbalanced = get_unbalanced(origin, tower)

    print(origin.name)
    print(origin.children)
    print(child_weights(origin, tower))


if __name__ == '__main__':
    with open('day07_input.txt') as file:
        day07_input = [Program(line) for line in file.readlines()]

    print(bottom(day07_input))
    print(corrected_weight(day07_input))
