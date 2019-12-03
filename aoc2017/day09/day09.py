import string


def solve(stream: string) -> tuple:
    """Returns the total score for all groups in stream and the number of characters
    in the garbage.
    Advent of Code 2017, day 9, part 1 and part 2."""
    score = 0
    garbage_score = 0
    layer = 1
    garbage = False

    i = 0
    while i < len(stream):
        if not garbage:
            if stream[i] == '{':
                score += layer
                layer += 1
            elif stream[i] == '}':
                layer -= 1
            elif stream[i] == '<':
                garbage = True
        else:
            if stream[i] == '!':
                i += 1
            elif stream[i] == '>':
                garbage = False
            else:
                garbage_score += 1
        i += 1

    return score, garbage_score


if __name__ == '__main__':
    with open('day09_input.txt') as file:
        day09_input = file.read()

    print(solve(day09_input))
