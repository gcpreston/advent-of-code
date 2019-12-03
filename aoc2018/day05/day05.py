import string


def main():
    with open('input.txt') as file:
        polymer = file.read().strip()

    print('Part 1:', part1(polymer))
    print('Part 2:', part2(polymer))


def part1(polymer: str):
    i = 0
    stack = []

    while i < len(polymer):
        curr = polymer[i]
        if stack != [] and different_cases(curr, stack[-1]):
            stack.pop()
            polymer = polymer[:i - 1] + polymer[i + 1:]
            i -= 2
        else:
            stack.append(curr)

        i += 1

    return len(stack)


def part2(polymer: str):
    return min([part1(polymer.replace(c, '').replace(c.upper(), '')) for c in string.ascii_lowercase])


def different_cases(s1, s2):
    if not (len(s1) == 1 and len(s2) == 1):
        return False
    else:
        return s1 == s2.swapcase()


if __name__ == '__main__':
    main()
