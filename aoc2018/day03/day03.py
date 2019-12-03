import re


def main():
    p = re.compile('#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
    with open('input.txt') as file:
        claims = []
        for line in file.readlines():
            m = re.match(p, line.strip())
            claims.append((int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5))))

    ans1, ans2 = solve(claims)
    print('Part 1:', ans1)
    print('Part 2:', ans2)


def solve(claims):
    fabric = [['.'] * 1000 for _ in range(1000)]
    no_overlap = set()
    count = 0

    for claim in claims:
        no_overlap.add(claim[0])

        for r in range(claim[4]):
            for c in range(claim[3]):
                row = claim[2] + r
                col = claim[1] + c
                f = fabric[row][col]

                if type(f) is int:
                    # already been visited exactly once
                    if f in no_overlap:
                        no_overlap.remove(f)
                    if claim[0] in no_overlap:
                        no_overlap.remove(claim[0])
                    count += 1
                    fabric[row][col] = 'X'
                elif f == '.':
                    fabric[row][col] = claim[0]

    return count, no_overlap.pop()


def part1(claims):
    return solve(claims)[0]


def part2(claims):
    return solve(claims)[1]


if __name__ == '__main__':
    main()
