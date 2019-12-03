import string


def solve_part1(nums: list, i: int, skip: int, ring: list, n: int=256) -> tuple:
    """Returns the product of the first two numbers in the resulting list.
    Advent of Code 2017, day 10, part 1."""
    for length in nums:
        ring = reverse(ring, length, i)
        i += length + skip
        i %= n
        skip += 1
    return ring, i, skip


def reverse(ring: list, length: int, i: int):
    """Reverses the section of ring starting at index i of length n."""
    if i + length > len(ring):
        section = ring[i:] + ring[:(i + length) % len(ring)]
        section = section[::-1]
        ring = (section[(len(ring) - i) % len(ring):]
                + ring[(i + length) % len(ring): i % len(ring)]
                + section[:(len(ring) - i) % len(ring)])
    elif i + length < len(ring):
        section = ring[i: i + length]
        section = section[::-1]
        ring = ring[:i] + section + ring[(i + length) % len(ring):]
    else:
        section = ring[i: i + length]
        section = section[::-1]
        ring = ring[:i] + section
    return ring


def knot_hash(s: string) -> string:
    """Generates the Knot Hash of the input.
    Advent of Code 2017, day 10, part 2."""
    nums = [ord(c) for c in s] + [17, 31, 73, 47, 23]
    i = 0
    skip = 0
    ring = list(range(256))

    for _ in range(64):
        if len(solve_part1(nums, i, skip, ring)[0]) == 512:
            print('what')
        ring, i, skip = solve_part1(nums, i, skip, ring)
    return dense_hash(ring)


def group(nums: list) -> list:
    """Returns nums with ever 16 elements grouped together."""
    grouped = []
    while nums:
        grouped.append(nums[:16])
        nums = nums[16:]
    return grouped


def xor_map(nums: list) -> int:
    """Calculates every number in nums XOR'd together."""
    total = 0
    for n in nums:
        total ^= n
    return total


def dense_hash(sparse: list) -> string:
    """Creates a dense hash out of the given sparse hash."""
    total_hash = ''
    for g in group(sparse):
        current_hash = xor_map(g)
        total_hash += f'{current_hash:02x}'
    return total_hash


if __name__ == '__main__':
    with open('day10_input.txt') as file:
        day10_input = file.read()

    part1_input = [int(n) for n in day10_input.split(',')]
    part1_data = solve_part1(part1_input, 0, 0, list(range(256)))

    print(part1_data[0][0] * part1_data[0][1])
    print(knot_hash(day10_input))
    # print(reverse([0, 1, 2, 3, 4], 2, 3))
