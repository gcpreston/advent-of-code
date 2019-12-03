def repeated_redist(banks: list) -> tuple:
    """Returns a two-element tuple. The first element is the number of redistribution cycles before
    the produced configuration has been seen before. The second element is the length of the infinite
    loop produced by the repeated configuration.
    Advent of Code 2017, day 6, parts 1 and 2."""

    def max_index(lst: list) -> int:
        """Returns the index of the max of lst."""
        highest = 0
        index = 0
        for i in range(len(lst)):
            if lst[i] > highest:
                highest = lst[i]
                index = i
        return index

    current = banks
    seen = []
    cycles = 0

    while current not in seen:
        seen.append(list(current))
        max_bank = max_index(current)
        buffer = current[max_bank]
        current[max_bank] = 0

        i = (max_bank + 1) % len(current)
        while buffer > 0:
            current[i] += 1
            i = (i + 1) % len(current)
            buffer -= 1

        cycles += 1

    return cycles, len(seen) - seen.index(current)


if __name__ == '__main__':
    with open('day06_input.txt') as file:
        day06_input = [int(n) for n in file.read().strip().split()]

    print(repeated_redist(day06_input))
