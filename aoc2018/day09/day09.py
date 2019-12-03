import re

from collections import deque, defaultdict


def main():
    p = re.compile(r'(\d+) players; last marble is worth (\d+) points')
    with open('input.txt') as file:
        m = p.match(file.read().strip())

    players = int(m.group(1))
    last = int(m.group(2))

    print('Part 1:', solve(players, last))
    print('Part 2:', solve(players, last * 100))


def solve(num_players: int, last_marble: int):
    circle = deque([0])
    marble = 1
    player = 1
    scores = defaultdict(int)

    def next_player():
        return (player % num_players) + 1

    while marble <= last_marble:
        if marble % 23 == 0:
            circle.rotate(7)
            scores[player] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)

        marble += 1
        player = next_player()

    return max([v for v in scores.values()])


if __name__ == '__main__':
    main()
