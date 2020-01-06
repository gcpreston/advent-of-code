import re
import math

from typing import Tuple, Dict, List, Union

Chemical = Tuple[str, int]  # i.e. ('ORE', 10)


def scaled_replace(c: Chemical, reactions: Dict[Chemical, List[Chemical]]) \
        -> List[Chemical]:
    """
    Example:
        >>> r = {('A', 2): [('B', 3), ('C', 4)]}
        >>> scaled_replace(('A', 6), r) == [('B', 9), ('C', 12)]
    """
    pass


def ore_needed(reactions: Dict[Chemical, List[Chemical]]) -> int:
    current: List[Union[Chemical, List[Chemical]]] = reactions[('FUEL', 1)]
    not_all_ore = True

    while not_all_ore:
        not_all_ore = False

        for i in range(len(current)):
            if current[i][0] != 'ORE':
                not_all_ore = True
                current[i] = scaled_replace(current[i], reactions)

        # flatten list of chemicals
        # https://stackoverflow.com/questions/952914
        current = [item for sublist in current for item in sublist]


def parse_chemicals(line: str) -> List[Chemical]:
    """
    Parse a list of Chemicals from a line of input text.
    """
    chemical_p = re.compile(r'(\d+) (\w+)')
    strs = re.split(r', | => ', line)

    parsed = list()
    for i in range(len(strs)):
        m = chemical_p.match(strs[i])
        parsed.append((m.group(2), int(m.group(1))))

    return parsed


def main(fn: str):
    # IDEA: part 1
    # Store input backwards: output chemical => [list of input chemicals]
    # This lets us start with what we want: 1 FUEL, and use hashing to figure
    # out what it would take to get this. For each sub-ingredient, we can figure
    # out what it takes to get each of those, and this tree expands until all
    # leaf nodes are ORE, at which point the sum of all leaves is computed.
    reactions = dict()

    with open(fn) as file:
        for line in file.readlines():
            chemicals = parse_chemicals(line.strip())
            reactions[chemicals[-1]] = chemicals[:-1]

    print('Part 1:', ore_needed(reactions))


if __name__ == '__main__':
    main('input/day14_test1.txt')
