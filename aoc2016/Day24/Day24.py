def main():
    with open('Day24_Input.txt') as file:
        maze = [line.rstrip() for line in file.readlines()]
        
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] == '0':
                print('START: (' + str(x) + ', ' + str(y) + ')')
            elif maze[y][x].isdigit():
                print(maze[y][x] + ': (' + str(x) + ', ' + str(y) + ')')
    
if __name__ == '__main__':
    main()