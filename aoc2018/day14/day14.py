def main():
    with open('input.txt') as file:
        recipe_num = int(file.read())

    print('Part 1:', part1(recipe_num))
    print('Part 2:', part2(str(recipe_num)))


def part1(recipe_num):
    recipes = [3, 7]
    elf1 = 0
    elf2 = 1

    while len(recipes) < recipe_num + 10:
        recipes += map(int, list(str(recipes[elf1] + recipes[elf2])))
        elf1 = (elf1 + recipes[elf1] + 1) % len(recipes)
        elf2 = (elf2 + recipes[elf2] + 1) % len(recipes)

    return ''.join(map(str, recipes[recipe_num: recipe_num + 10]))


def part2(scores):
    recipes = '37'
    elf1 = 0
    elf2 = 1

    while scores not in recipes[-7:]:
        recipes += str(int(recipes[elf1]) + int(recipes[elf2]))
        elf1 = (elf1 + int(recipes[elf1]) + 1) % len(recipes)
        elf2 = (elf2 + int(recipes[elf2]) + 1) % len(recipes)

    return recipes.index(scores)


if __name__ == '__main__':
    main()
