def main():
    with open('Day25_Input.txt') as file:
        contents = [l.rstrip().split(' ') for l in file]
        
    a = 0
    registry = {'a': a, 'b': 0, 'c': 0, 'd': 0}
    clock = []
    
    found = False
    while not found:
        i = 0
        while i < len(contents):
            if contents[i][0] == 'cpy':
                try:
                    int(contents[i][1])
                    is_digit = True
                except:
                    is_digit = False
                if is_digit:
                    registry[contents[i][2]] = int(contents[i][1])
                else:
                    registry[contents[i][2]] = registry[contents[i][1]]
            elif contents[i][0] == 'inc':
                registry[contents[i][1]] += 1
            elif contents[i][0] == 'dec':
                registry[contents[i][1]] -= 1
            elif contents[i][0] == 'out':
                if registry[contents[0][1]] != '0' and registry[contents[0][1]] != '1':
                    print('FAILED:', a)
                    break
                clock.append(registry[contents[0][1]])
                if len(clock) == 100:
                    print(a, clock)
            else:
                if contents[i][1].isalpha() and registry[contents[i][1]] != 0:
                    i += int(contents[i][2]) - 1
                elif contents[i][1].isdigit() and int(contents[i][1]) != 0:
                    i += int(contents[i][2]) - 1
            i += 1
        a += 1
        registry = {'a': a, 'b': 0, 'c': 0, 'd': 0}
    
if __name__ == '__main__':
    main()