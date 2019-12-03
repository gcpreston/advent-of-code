def checksum(data: list) -> int:
    """Finds the checksum of the 2D list of numbers.
    Advent of Code 2017, day 2, part 1."""
    total = 0
    for row in data:
        total += (max(row) - min(row))
    return total


def div_sum(data: list) -> int:
    """Finds the sum of the division of the only evenly divisible numbers in each row.
    Advent of Code 2017, day 2, part 2."""

    def even_quotient(nums: list) -> int:
        """Finds the quotient of the only two numbers in the list that evennly divide."""
        for i in range(len(nums[:-1])):
            for j in range(i + 1, len(nums)):
                if nums[i] % nums[j] == 0:
                    return nums[i] // nums[j]
                elif nums[j] % nums[i] == 0:
                    return nums[j] // nums[i]

    total = 0
    for row in data:
        total += even_quotient(row)
    return total


if __name__ == '__main__':
    with open('day02_input.txt') as file:
        day02_input = [line.strip().split('\t') for line in file.readlines()]
    parsed = []
    for line in day02_input:
        current_line = []
        for n in line:
            current_line.append(int(n))
        parsed.append(current_line)

    print(checksum(parsed))
    print(div_sum(parsed))
