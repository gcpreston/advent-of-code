def main():
    with open('input.txt') as file:
        coords = [tuple(int(s) for s in line.strip().split(', ')) for line in file.readlines()]

    print('Part 1:', part1(coords))


def part1(coords):
    min_x = coords[0][0]
    max_x = coords[0][0]
    min_y = coords[0][1]
    max_y = coords[0][1]

    for c in coords:
        if c[0] < min_x:
            min_x = c[0]
        elif c[0] > max_x:
            max_x = c[0]

        if c[1] < min_y:
            min_y = c[1]
        elif c[1] > max_y:
            max_y = c[1]

    counts = [0 for _ in range(len(coords))]

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            i = closest((x, y), coords)

            if i != -1:
                counts[i] += 1
    print(counts)
    return max(counts)


def distance(c1, c2):
    """
    Compute the Manhattan distance between two 2-tuples representing points on a coordinate plane.

    :param c1: the first coordinate
    :param c2: the second coordinate
    :return: the Manhattan distance between c1 and c2
    """
    return abs(c2[0] - c1[0]) + abs(c2[1] - c1[1])


def closest(c, coords):
    """
    Find the index of the coordinate in coords with the lowest distance to c.

    :param c: the point to find the closest coordinate to
    :param coords: the coordinates
    :return: the index of the closest coordinate in coords, -1 if c is in coords
    """
    best = 0
    best_distance = distance(c, coords[0])
    for i in range(1, len(coords)):
        c2 = coords[i]
        d = distance(c, c2)

        if d < best_distance:
            best = i
            best_distance = d
    return best


def part2(coords):
    pass


if __name__ == '__main__':
    main()
