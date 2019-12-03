def main():
    with open('Day22_Input.txt') as file:
        nodes = [line.rstrip().split() for line in file.readlines() if line.startswith('/dev')]
    
    map = [['.' for _ in range(38)] for _ in range(28)]
    
    for n in nodes:
        coordinates = [int(c[1:]) for c in n[0].split('-') if not c.startswith('/dev')]
        if coordinates == [37, 0]:
            map[coordinates[1]][coordinates[0]] = 'G'
        elif n[2] == '0T':
            map[coordinates[1]][coordinates[0]] = '_'
        elif len(n[1]) >= 4:
            map[coordinates[1]][coordinates[0]] = '#'
        
    file = open('map.txt', 'w')
    for l in map:
        file.write(''.join(l) + '\n')
        
    # Get to G in 80 moves, move it once in 81.
    # Starting behind G, it takes 5 moves to move it once.
    # Need to move it 36 times after turn 81, 5(36) + 81 = 261
    print('Map written to map.txt')
    
def part1(nodes):
    count = 0
    for A in range(len(nodes)):
        used = int(nodes[A][2][:-1])
        if used != 0:
            for B in range(len(nodes)):
                if A != B and int(nodes[B][3][:-1]) >= used:
                    count += 1
    # Part 1
    print(count)

if __name__ == '__main__':
    main()