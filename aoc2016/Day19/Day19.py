# from math import log

def main():
    # input = 3004953
    input = 1000
    for n in range(1, input):
        print(n, take_across(n))
    
# Actually simulating this SUCKS, just do the math
def take_across(num_elves):
    return
    #===========================================================================
    # winner = 1
    # for n in range(1, num_elves + 1):
    #     if log(n, 3) == int(log(n, 3)):
    #         winner = 1
    #===========================================================================
        
    
def rotate(l, n):
    return l[n:] + l[:n]
        
if __name__ == '__main__':
    main()