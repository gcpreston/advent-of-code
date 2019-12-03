import copy


class Scanner:

    def __init__(self, depth: int, range: int):
        self.depth = depth
        self.range = range
        self.index = 0
        self.direction = -1

    def move(self):
        if self.index == self.range - 1 or self.index == 0:
            self.direction *= -1
        self.index += self.direction

    def distance_to_0(self):
        if self.direction == -1:
            return self.index
        else:
            return 2 * (self.range - 1) - self.index


def severity(firewall: list) -> int:
    """Calculates the severity of the trip through the firewall starting at picosecond 0.
    Advent of Code 2017, day 13, part 1."""
    scanners = [Scanner(i, firewall[i]) if firewall[i] != 0 else None for i in range(len(firewall))]
    pico = 0
    layer = 0
    caught = []

    while layer < len(firewall):
        # display(firewall, pico, layer, scanners)
        if scanners[layer] and scanners[layer].index == 0:
            caught.append(layer)
        for s in scanners:
            if s:
                s.move()
        layer += 1
        pico += 1

    total = 0
    for c in caught:
        total += c * firewall[c]
    return total


def passes(firewall: list, scanners: list=None) -> bool:
    """Checks if the packet is able to pass through the given firewall configuration."""
    if not scanners:
        scanners = [Scanner(i, firewall[i]) if firewall[i] != 0 else None for i in range(len(firewall))]

    for depth in range(len(firewall)):
        if scanners[depth]:
            d = scanners[depth].distance_to_0()
            f = 2 * (firewall[depth] - 1)
            if (depth - d) % f == 0:
                return False
    return True


def delay(firewall: list) -> int:
    """Computes the fewest number of picoseconds you must delay to pass through the
    firewall without getting caught.
    Advent of Code 2017, day 13, part 2."""
    pico = 0
    scanners = [Scanner(i, firewall[i]) if firewall[i] != 0 else None for i in range(len(firewall))]
    while not passes(firewall, scanners):
        # display(firewall, pico, -1, scanners)
        pico += 1
        for s in scanners:
            if s:
                s.move()
    return pico


def display(firewall: list, pico: int, layer: int, scanners: list) -> None:
    """Displays the current state of the packet moving through the firewall."""
    print(f'Picosecond {pico}:')
    for n in range(len(firewall)):
        print(f' {n}  ', end='')
    print()

    for d in range(max(firewall)):
        for i in range(len(firewall)):
            if not scanners[i]:
                if d == 0:
                    if i == layer:
                        print('(.) ', end='')
                    else:
                        print('... ', end='')
                else:
                    print('    ', end='')
            elif scanners[i].index == d:
                if i == layer and d == 0:
                    print('(S) ', end='')
                else:
                    print('[S] ', end='')
            elif scanners[i].range > d:
                if i == layer and d == 0:
                    print('( ) ', end='')
                else:
                    print('[ ] ', end='')
            else:
                print('    ', end='')
        print()
    print()


if __name__ == '__main__':
    with open('day13_input.txt') as file:
        lines = file.readlines()
        deepest = int(lines[-1].split(': ')[0])
        day13_input = [0 for _ in range(deepest + 1)]
        for line in lines:
            data = [int(n) for n in line.split(': ')]
            day13_input[data[0]] = data[1]

    print(severity(day13_input))
    print(delay(day13_input))

