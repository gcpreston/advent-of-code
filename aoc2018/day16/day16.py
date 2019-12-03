def main():
    with open('input.txt') as file:
        contents = file.read()

    raw_samples = contents.split('\n\n\n')[0].split('\n\n')
    samples = [(eval(b[8:]), [int(n) for n in o.split()], eval(a[7:]))
               for b, o, a in [sample.split('\n') for sample in raw_samples]]

    print('Part 1:', part1(samples))


def part1(samples):
    ops = [addr, addi,
           mulr, muli,
           banr, bani,
           borr, bori,
           setr, seti,
           gtir, gtri, gtrr,
           eqir, eqri, eqrr]

    total = 0
    for before, instruction, after in samples:
        opcode, a, b, c = instruction
        count = 0

        for f in ops:
            if f(before, a, b, c) == after:
                count += 1

        if count >= 3:
            total += 1

    return total


def opr(f):
    def oprf(before, a, b, c):
        after = list(before)
        after[c] = f(before[a], before[b])
        return after
    return oprf


def opi(f):
    def opif(before, a, b, c):
        after = list(before)
        after[c] = f(before[a], b)
        return after
    return opif


def op(f):
    return opr(f), opi(f)


addr, addi = op(lambda x, y: x + y)
mulr, muli = op(lambda x, y: x * y)
banr, bani = op(lambda x, y: x & y)
borr, bori = op(lambda x, y: x | y)


def setr(before, a, _, c):
    after = list(before)
    after[c] = before[a]
    return after


def seti(before, a, _, c):
    after = list(before)
    after[c] = a
    return after


def gtir(before, a, b, c):
    after = list(before)
    if a > before[b]:
        after[c] = 1
    else:
        after[c] = 0
    return after


def gtri(before, a, b, c):
    after = list(before)
    if before[a] > b:
        after[c] = 1
    else:
        after[c] = 0
    return after


def gtrr(before, a, b, c):
    after = list(before)
    if before[a] > before[b]:
        after[c] = 1
    else:
        after[c] = 0
    return after


def eqir(before, a, b, c):
    after = list(before)
    if a == before[b]:
        after[c] = 1
    else:
        after[c] = 0
    return after


def eqri(before, a, b, c):
    after = list(before)
    if before[a] == b:
        after[c] = 1
    else:
        after[c] = 0
    return after


def eqrr(before, a, b, c):
    after = list(before)
    if before[a] == before[b]:
        after[c] = 1
    else:
        after[c] = 0
    return after


if __name__ == '__main__':
    main()
