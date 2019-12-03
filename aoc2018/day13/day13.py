class Cart:

    def __init__(self, direction: str, x: int, y: int):
        self._facings = ['<', '^', '>', 'v']
        self.d = direction
        self.x = x
        self.y = y
        self._lastturn = 1  # -1 = left, 0 = straight, 1 = right

    def next_coord(self):
        before = (self.x, self.y)

        self.move()
        after = (self.x, self.y)

        self.x, self.y = before
        return after

    def move(self):
        if self.d == '^':
            self.y -= 1
        elif self.d == 'v':
            self.y += 1
        elif self.d == '<':
            self.x -= 1
        else:
            self.x += 1

    def intersection(self):
        self._lastturn = ((self._lastturn + 1) % 3) - 1
        self.d = self._facings[self._facings.index(self.d) + self._lastturn]

    def __repr__(self):
        return f'Cart({self.d}, {self.x}, {self.y})'


def main():
    track, carts = parse_input('input.txt')
    print(track, carts)

    part1_x, part1_y = firstcrash(track, carts)
    print(f'Part 1: {part1_x},{part1_y}')


def parse_input(fn):
    with open(fn) as file:
        initial = [line.replace('\n', '') for line in file.readlines()]

    facings_lr = {'<', '>'}
    facings_ud = {'^', 'v'}
    carts = []

    for r in range(len(initial)):
        for c in range(len(initial[r])):

            if initial[r][c] in facings_lr:
                carts.append(Cart(initial[r][c], c, r))
                initial[r] = initial[r][:c] + '-' + initial[r][c + 1:]
            elif initial[r][c] in facings_ud:
                carts.append(Cart(initial[r][c], c, r))
                initial[r] = initial[r][:c] + '|' + initial[r][c + 1:]

    return initial, carts


def firstcrash(track, carts):
    facings = {'<', '^', '>', 'v'}

    while True:
        carts.sort(key=lambda item: (item.y, item.x))

        for cart in carts:
            n_c = cart.next_coord()


if __name__ == '__main__':
    main()
