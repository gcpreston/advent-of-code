def main():
    with open('input.txt') as file:
        serial = int(file.read())

    part1_x, part1_y, _ = maxsquare(3, 300, 300, serial)
    print(f'Part 1: {part1_x},{part1_y}')
    print('Part 2:', ','.join(str(c) for c in maxmaxsquare(300, 300, serial)))


def maxmaxsquare(width, height, serial):
    grid = gengrid(width, height, serial)

    max_x = 0
    max_y = 0
    max_s = 0
    biggest = 0

    # TODO: Make cumulative sum variable

    for s in range(5, min(width, height) + 1):
        print(s)
        x, y, current = maxsquare(s, width, height, serial, grid=grid)
        if current > biggest:
            biggest = current
            max_x = x
            max_y = y
            max_s = s

    return max_x, max_y, max_s


def maxsquare(s, width, height, serial, grid=None):
    if not grid:
        grid = gengrid(width, height, serial)

    max_x = 0
    max_y = 0
    biggest = 0

    for r in range(1, height + 1 - s):

        for c in range(1, width + 1 - s):
            current = squaresum(s, grid, c, r)
            if current > biggest:
                biggest = current
                max_x = c + 1
                max_y = r + 1

    return max_x, max_y, biggest


def squaresum(s, grid, x, y):
    """
    Calculate the sum power levels of fuel cells in the s x s square whose top-
    left corner is at x,y.

    :param s: the side length of the square
    :param grid: the grid of fuel cell power levels
    :param x: the x coordinate of the top-left corner
    :param y: the y coordinate of the top-left corner
    :return: the sum of the power levels in specified area
    """
    total = 0

    for r in range(y, y + s):
        for c in range(x, x + s):
            total += grid[r][c]

    return total


def gengrid(width, height, serial):
    grid = []

    for y in range(height):
        grid.append([])

        for x in range(width):
            grid[y].append(powerlevel(x + 1, y + 1, serial))

    return grid


def powerlevel(x: int, y: int, serial: int):
    rackid = x + 10
    power = rackid * y
    power += serial
    power *= rackid
    power = int(str(power)[-3])
    return power - 5


if __name__ == '__main__':
    main()
