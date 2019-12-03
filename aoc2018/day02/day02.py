def main():
    with open('input.txt') as file:
        boxes = [line.strip() for line in file.readlines()]

    print('Part 1:', part1(boxes))
    print('Part 2:', part2(boxes))


def part1(boxes):
    two_count = 0
    three_count = 0

    for b in boxes:
        letters = counts(b)
        if 2 in letters.values():
            two_count += 1
        if 3 in letters.values():
            three_count += 1
    return two_count * three_count


def counts(s):
    letters = dict()
    for c in s:
        if c in letters:
            letters[c] += 1
        else:
            letters[c] = 1
    return letters


def part2(boxes):
    subs = set()
    for b in boxes:

        b_subs = set()
        for i in range(len(b)):
            s = b[:i] + b[i+1:]
            b_subs.add(s)

            if s in subs:
                return s

        subs.update(b_subs)


def match(s1, s2):
    """
    Determine if two strings differ by exactly one character.
    Source: https://stackoverflow.com/questions/25216328/compare-strings-allowing-one-character-difference

    :param s1: the first string
    :param s2: the second string
    :return: True if s1 and s2 differ by exactly one character, False otherwise
    """
    ok = False
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            if ok:
                return False
            else:
                ok = True
    return True


if __name__ == '__main__':
    main()