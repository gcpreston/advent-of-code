def main():
    with open('Day08_Input.txt') as file:
        contents = [l.rstrip().split(' ') for l in file.readlines()]

    screen = [['.' for _ in range(50)] for _ in range(6)]
    for line in contents:
        if line[0] == 'rect':
            dimensions = [int(n) for n in line[1].split('x')]
            for c in range(dimensions[0]):
                for r in range(dimensions[1]):
                    screen[r][c] = '#'
                    
        else:
            if line[1] == 'row':
                index = int(line[2][2:])
                screen[index] = rotate_row(screen[index], int(line[4]))
            else:
                index = int(line[2][2:])
                screen = rotate_col(screen, index, int(line[4]))
                  
    count = 0           
    for r in range(len(screen)):
        for c in range(len(screen[0])):
            if screen[r][c] == '#':
                count += 1
                print(screen[r][c], end='')
            else:
                print(' ', end='')
        print()
    print(str(count) + ' pixels')
    
def rotate_row(l, n):
    return l[-n:] + l[:-n]

def rotate_col(screen, c, n):
    col = []
    for r in screen:
        col.append(r[c])
    col = rotate_row(col, n)
    for r in range(len(screen)):
        screen[r][c] = col[r]
    return screen

if __name__ == '__main__':
    main()