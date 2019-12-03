def main():
    map = ['.^^^^^.^^.^^^.^...^..^^.^.^..^^^^^^^^^^..^...^^.^..^^^^..^^^^...^.^.^^^^^^^^....^..^^^^^^.^^^.^^^.^^']

    for i in range(399999):
        map.append(next_row(map[i]))
        
    count = 0
    for row in map:
        for tile in row:
            if tile == '.':
                count += 1
    print(count)
    
def next_row(row):
    next = ''
    for i in range(len(row)):
        if i == 0:
            left = '.'
            right = row[i + 1]
        elif i == len(row) - 1:
            left = row[i - 1]
            right = '.'
        else:
            left = row[i - 1]
            right = row[i + 1]
        center = row[i]
        
        if ((left == '^' and center == '^' and right == '.') or
            (left == '.' and center == '^' and right == '^') or
            (left == '^' and center == '.' and right == '.') or
            (left == '.' and center == '.' and right == '^')):
            next += '^'
        else:
            next += '.'
    return next
    
if __name__ == '__main__':
    main()