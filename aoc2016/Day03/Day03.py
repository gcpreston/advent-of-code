def main():
    with open('Day03_Input.txt') as file:
        contents = file.readlines()
        
    sides = []
    for line in contents:
        sides.append([int(n.strip()) for n in line.split('  ') if not n.strip() == ''])
        
    count = 0
    for triangle in sides:
        triangle = sorted(triangle)
        if triangle[0] + triangle[1] > triangle[2]:
            count += 1
    
    print('Possible triangles (part 1):', count)
    
    count = 0
    for c in range(len(sides[0])):
        r = 0
        while r < len(sides):
            current = sorted([sides[r][c], sides[r+1][c], sides[r+2][c]])
            if current[0] + current[1] > current[2]:
                count += 1
            r += 3
    
    print('Possible triangles (part 2):', count)
    
if __name__ == '__main__':
    main()