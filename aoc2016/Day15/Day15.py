def main():
    # Disc # = index of tuple + 1, number of positions = tuple index 0, number of ticks from hole = tuple index 1
    discs = [(13, 2), (5, 0), (17, 6), (3, 0), (7, 5), (19, 2), (11, 0)]
    time = 0
    
    found = False
    while not found:
        if check_time(time, discs):
            found = True
            print(time)
        time += 1
        
def check_time(time, discs):
    for i in range(len(discs)):
        if (time + i + 1 - discs[i][1]) % discs[i][0] != 0:
            return False
    return True
    
if __name__ == '__main__':
    main()