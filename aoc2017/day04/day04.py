import string


def valid_passphrase_v1(pwd: string) -> bool:
    """Checks if pwd has no repeated words.
    Advent of Code 2017, day 4, part 1."""
    words = pwd.split()
    unique = set(words)
    if len(words) == len(unique):
        return True
    return False


def valid_passphrase_v2(pwd: string) -> bool:
    """Checks if no words in pwd can be rearranged to be any other word in pwd.
    Advent of Code 2017, day 4, part 2."""
    words = [sorted(list(w)) for w in pwd.split()]
    for i in range(len(words)):
        if words[i] in words[i+1:]:
            return False
    return True


if __name__ == '__main__':
    with open('day04_input.txt') as file:
        day02_input = file.readlines()

    part1_count = 0
    part2_count = 0
    for phrase in day02_input:
        if valid_passphrase_v1(phrase):
            part1_count += 1
        if valid_passphrase_v2(phrase):
            part2_count += 1

    print(part1_count)
    print(part2_count)
