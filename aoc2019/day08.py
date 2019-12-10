from typing import List

w = 25
h = 6


def chunks(lst, n):
    """https://stackoverflow.com/questions/312443"""
    for i in range(0, len(lst), n):
        yield lst[i:i+n]


def appearances(layer: List[int], n: int) -> int:
    """
    Count the number of times ``n`` appears in ``layer``.
    """
    c = 0
    for k in layer:
        if k == n:
            c += 1
    return c


def part1(data: List[List[int]]) -> int:
    fewest = w * h
    fewest_i = 0

    for i in range(len(data)):
        count = appearances(data[i], 0)
        if count < fewest:
            fewest = count
            fewest_i = i

    return appearances(data[fewest_i], 1) * appearances(data[fewest_i], 2)


def decode(data: List[List[int]]) -> List[int]:
    current: List[int] = data[0].copy()

    for i in range(len(data)):
        layer = data[i]

        # Check for currently transparent pixels
        for j in range(len(current)):
            if current[j] == 2:
                if layer[j] == 0 or layer[j] == 1:
                    current[j] = layer[j]
    return current


def main(fn: str):
    # Parse into list of layers
    with open(fn) as file:
        data = list(chunks([int(c) for c in file.read().strip()], w * h))
        print(f'{data[0][0]=}')

    print('Part 1:', part1(data))
    print('Part 2:')

    mapping = {0: ' ', 1: '#'}
    decoded = decode(data)
    for r in range(h):
        for c in range(w):
            print(mapping[decoded[(r * w) + c]], end='')
        print()


if __name__ == '__main__':
    main('input/day08.txt')
