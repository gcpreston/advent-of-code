import string


def captcha_solution_v1(captcha: string) -> int:
    """Calculates the sum of all digits that match the next digit in the string.
    Advent of Code 2017, day 1, part 1."""
    total = 0
    for i in range(len(captcha)):
        if captcha[i] == captcha[(i + 1) % len(captcha)]:
            total += int(captcha[i])
    return total


def captcha_solution_v2(captcha: string) -> int:
    """Calculates the sum of all digits that match the digit halfway around the circular string.
    Advent of Code 2017, day 1, part 2."""
    total = 0
    for i in range(len(captcha)):
        if captcha[i] == captcha[(i + (len(captcha) // 2)) % len(captcha)]:
            total += int(captcha[i])
    return total

if __name__ == '__main__':
    with open('day01_input.txt') as file:
        day01_input = file.read().strip()

    print(captcha_solution_v1(day01_input))
    print(captcha_solution_v2(day01_input))
