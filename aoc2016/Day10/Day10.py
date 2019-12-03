def main():
    with open('Day10_Input.txt') as file:
        contents = [l.rstrip().split(' ') for l in file.readlines()]
    
    bots = [[None, None] for _ in range(209)]
    output = [[] for _ in range(25)]

    while True:
        if output[0] and output[1] and output[2]:
            print(output[0][0] * output[1][0] * output[2][0])
            break      
        for l in contents:
            if l[0] == 'value':
                bot_num = int(l[5]) - 1
                if bots[bot_num][0] == None:
                    bots[bot_num][0] = int(l[1])
                else:
                    bots[bot_num][1] = int(l[1])
                del contents[contents.index(l)]
            else:
                bot = int(l[1]) - 1
                low = int(l[6]) - 1
                high = int(l[11]) - 1
                if bots[bot][0] != None and bots[bot][1] != None:
                    if 61 in bots[bot] and 17 in bots[bot]:
                        print(bot + 1)
                    if l[5] == 'bot':
                        if bots[low][0] == None:
                            bots[low][0] = min(bots[bot])
                        else:
                            bots[low][1] = min(bots[bot])
                    else:
                        output[low + 1].append(min(bots[bot]))
                    if l[10] == 'bot':
                        if bots[high][0] == None:
                            bots[high][0] = max(bots[bot])
                        else:
                            bots[high][1] = max(bots[bot])
                    else:
                        output[high + 1].append(max(bots[bot]))
                    bots[bot] = [None, None]
                        
if __name__ == '__main__':
    main()