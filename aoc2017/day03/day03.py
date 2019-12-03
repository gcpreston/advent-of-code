def steps(n: int) -> int:
    """Calculates the Manhattan Distance between n and 1.
    Advent of Code 2017, day 3, part 1."""

    def smaller_odd_square(num: int) -> int:
        """Finds the largest odd n such that n^2 < num."""
        current = 1
        while (current + 2)**2 < num:
            current += 2
        return current

    def adj_distances(shell_num: int) -> list:
        """Creates a list of the form [shell_num - 1, shell_num - 2, ..., 0, 1, ..., shell_num]."""
        if shell_num == 0:
            return [0, 1]

        d = [shell_num - 1]
        while d[-1] != 0:
            d.append(d[-1] - 1)
        for i in range(1, shell_num + 1):
            d.append(i)
        return d

    if n == 1:
        return 0

    square = smaller_odd_square(n)
    shell = (square + 1) // 2
    index = n - (square**2 + 1)
    distances = adj_distances(shell)
    adj = distances[index % len(distances)]

    return shell + adj


def first_larger(n: int) -> int:
    """Returns the first vaue written larger than n.
    Advent of Code 2017, day 3, part 2."""

    def sum_of_adjacents(data: dict, key: tuple) -> int:
        """Calculates the sum of the adjacent squares in the spiral."""
        adjacents = [(key[0] - 1, key[1] + 1), (key[0] + 0, key[1] + 1), (key[0] + 1, key[1] + 1),
                     (key[0] - 1, key[1] + 0), (key[0] + 1, key[1] + 0),
                     (key[0] - 1, key[1] - 1), (key[0] + 0, key[1] - 1), (key[0] + 1, key[1] - 1)]

        total = 0
        for a in adjacents:
            try:
                total += data[a]
            except KeyError:
                pass
        return total

    width = 0
    height = 0
    current_key = (0, 0)
    spiral = {current_key: 1}
    next_value = 1

    # this coruld definitely be written in a better way
    while next_value <= n:
        while current_key[0] <= width:
            current_key = (current_key[0] + 1, current_key[1])
            next_value = sum_of_adjacents(spiral, current_key)
            spiral[current_key] = next_value
            if next_value > n:
                return next_value
        width += 1

        while current_key[1] <= height:
            current_key = (current_key[0], current_key[1] + 1)
            next_value = sum_of_adjacents(spiral, current_key)
            spiral[current_key] = next_value
            if next_value > n:
                return next_value
        height += 1

        while current_key[0] > (-1 * width):
            current_key = (current_key[0] - 1, current_key[1])
            next_value = sum_of_adjacents(spiral, current_key)
            spiral[current_key] = next_value
            if next_value > n:
                return next_value

        while current_key[1] > (-1 * height):
            current_key = (current_key[0], current_key[1] - 1)
            next_value = sum_of_adjacents(spiral, current_key)
            spiral[current_key] = next_value
            if next_value > n:
                return next_value

    return spiral[current_key]


if __name__ == '__main__':
    day03_input = 265149
    print(steps(day03_input))
    print(first_larger(day03_input))
