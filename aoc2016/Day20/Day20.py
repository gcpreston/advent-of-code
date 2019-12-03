def main():
    with open("Day20_Input.txt") as file:
        blacklist = [[int(n) for n in l.rstrip().split('-')] for l in file.readlines()]

    count = 0
    i = 0
    while i < 4294967295:
        i += 1
        blocked = False
        for r in blacklist:
            if r[0] <= i <= r[1]:
                i = r[1]
                blocked = True
                break
        if not blocked:
            print('WORKS:', i)
            count += 1
    print(count)
    
if __name__ == '__main__':
    main()