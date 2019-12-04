def encode(n: int) -> str:
    """
    Ex:
    111122 -> 1422
    123444 -> 11213143
    """
    new: str = ""
    count: int = 0
    prev: str = ""

    for d in str(n):
        if d == prev:
            count += 1
        else:
            if count > 0:
                new += prev + str(count)
            prev = d
            count = 1

    new += prev + str(count)
    return new


def valid_count(a: int, b: int, exact: bool) -> int:
    count = 0

    for n in range(a, b + 1):
        # encoding first is not the fastest but it makes things a little easier
        s = encode(n)

        repeat = False
        decrease = False

        prev = -1
        for i in range(0, len(s), 2):
            d = int(s[i])
            r = int(s[i + 1])

            if (exact and r == 2) or (not exact and r >= 2):
                repeat = True
            if d < prev:
                decrease = True
                break
            prev = d

        if repeat and not decrease:
            count += 1

    return count


def main(fn: str):
    with open(fn) as file:
        a, b = [int(i) for i in file.read().split('-')]

    print('Part 1:', valid_count(a, b, False))
    print('Part 2:', valid_count(a, b, True))


if __name__ == '__main__':
    main('input/day04.txt')
