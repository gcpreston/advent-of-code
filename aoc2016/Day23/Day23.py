def main():
    with open('Day23_Input.txt') as file:
        contents = [l.rstrip().split(' ') for l in file]
        
    registry = {'a': 12, 'b': 0, 'c': 0, 'd': 0}
    
    i = 0
    while i < len(contents):
        if i == 4:
            registry['a'] = int(registry['b']) * int(registry['d'])
            registry['c'] = 0
            registry['d'] = 0
            i += 6
            continue
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
        elif contents[i][0] == 'tgl':
            if i + registry[contents[i][1]] < len(contents):
                if len(contents[i+registry[contents[i][1]]]) == 2:
                    if contents[i+registry[contents[i][1]]][0] == 'inc':
                        contents[i+registry[contents[i][1]]][0] = 'dec'
                    else:
                        contents[i+registry[contents[i][1]]][0] = 'inc'
                else:
                    if contents[i+registry[contents[i][1]]][0] == 'jnz':
                        contents[i+registry[contents[i][1]]][0] = 'cpy'
                    else:
                        contents[i+registry[contents[i][1]]][0] = 'jnz'
        else:
            if contents[i][1].isalpha() and registry[contents[i][1]] != 0:
                i += int(contents[i][2]) - 1
            elif contents[i][1].isdigit() and int(contents[i][1]) != 0:
                i += registry[contents[i][2]] - 1
        i += 1
        # print('Line: ' + str(i) + ', c: ' + str(registry['c']) + ', d: ' + str(registry['d']))
    print(registry['a'])
    
if __name__ == '__main__':
    main()