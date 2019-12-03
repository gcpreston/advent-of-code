import re

from collections import deque


def main():
    # data is a list of lists, each containing a list with position coordinates
    # and a tuple with velocity deltas
    data = []

    with open('input.txt') as file:

        for line in file.readlines():
            x, y, dx, dy = map(int, re.findall(r'-*\d+', line))
            data.append([[x, y], (dx, dy)])

    # Find the most likely frame by area: 10369
    # areas = []
    # for _ in range(100000):
    #     areas.append(area(data))
    #     tick(data)

    # m = min(areas)
    # print(m, areas.index(m))

    for _ in range(10369):
        tick(data)

    render(data)
    print(10369)


def area(data):
    coords = [pos for pos, _ in data]

    x_vals = [x for x, _ in coords]
    y_vals = [y for _, y in coords]

    min_x = min(x_vals)
    max_x = max(x_vals)
    min_y = min(y_vals)
    max_y = max(y_vals)

    return (max_x - min_x) * (max_y - min_y)


def tick(data):
    for t in data:
        t[0] = [sum(pair) for pair in zip(t[0], t[1])]


def render(data, fn=None):
    coords = [pos for pos, _ in data]
    # coords.sort(key=lambda c: (c[1], c[0]))

    x_vals = [x for x, _ in coords]
    y_vals = [y for _, y in coords]

    min_x = min(x_vals)
    # max_x = max(x_vals)
    min_y = min(y_vals)
    max_y = max(y_vals)

    out = ''
    for y in range(min_y, max_y + 1):
        vals = deque(sorted([c[0] for c in coords if c[1] == y]))

        prev = min_x - 1
        while vals:
            v = vals.popleft()
            if v != prev:
                out += '.' * (v - prev - 1)
                out += '#'
                prev = v
        out += '\n'

    if fn:
        with open(fn, 'w') as file:
            file.write(out)
    else:
        print(out)


if __name__ == '__main__':
    main()
