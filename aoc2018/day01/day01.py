def main():
    with open('input.txt') as file:
        nums = [int(n) for n in file.read().strip().split('\n') if n != '']

    print('Part 1:', part1(nums))
    print('Part 2:', part2(nums))


def part1(nums):
    return sum(nums)


def part2(nums):
    total = 0
    vals = set()

    i = 0
    while total not in vals:
        vals.add(total)
        total += nums[i]
        if i == len(nums) - 1:
            i = 0
        else:
            i += 1

    return total


if __name__ == '__main__':
    main()
