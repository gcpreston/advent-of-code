def main():
    with open('Day12_Input.txt') as file:
        contents = [l.rstrip().split(' ') for l in file]
        
    registry = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
    
    i = 0
    while i < len(contents):
        if contents[i][0] == 'cpy':
            if contents[i][1].isdigit():
                registry[contents[i][2]] = int(contents[i][1])
            else:
                registry[contents[i][2]] = registry[contents[i][1]]
        elif contents[i][0] == 'inc':
            registry[contents[i][1]] += 1
        elif contents[i][0] == 'dec':
            registry[contents[i][1]] -= 1
        else:
            if registry[contents[i][1]] != 0:
                i += int(contents[i][2]) - 1
        i += 1
    print(registry['a'])
    
if __name__ == '__main__':
    main()