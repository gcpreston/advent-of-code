def main():
    with open('Day06_Input.txt') as file:
        contents = [[c for c in l if c != '\n'] for l in file.readlines()]
    
    message = ''
    for c in range(len(contents[0])):
        counts = {}
        for r in range(len(contents)):
            if not contents[r][c] in counts:
                counts[contents[r][c]] = 1
            else:
                counts[contents[r][c]] += 1
                
        min = 572
        for c in counts:
            if counts[c] < min:
                min = counts[c]
                min_letter = c
        message += min_letter
    print(message)
    
if __name__ == '__main__':
    main()