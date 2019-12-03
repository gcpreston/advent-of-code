class Node:

    def __init__(self):
        self.children = []
        self.metadata = []

    @classmethod
    def from_nums(cls, nums):
        ret = cls()

        for i in range(1, nums[1] + 1):
            ret.add_metadata(nums[-1 * i])
        return ret

    def add_child(self, c: 'Node'):
        self.children.append(c)

    def add_metadata(self, m: int):
        self.metadata.append(m)


def main():
    with open('input.txt') as file:
        nums = [int(n) for n in file.read().strip().split()]

    print('Part 1:', part1(nums))


def part1(nums):
    return Node.from_nums(nums).metadata


def part2():
    pass


if __name__ == '__main__':
    main()
