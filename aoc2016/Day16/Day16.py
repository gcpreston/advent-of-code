def main():
    # length = 273
    length = 35651584
    a = '01110110101001000'

    while len(a) < length:
        a = extend(a)
        print(len(a))
    print('Extend finished.')
    a = a[:length]
    
    cs = checksum(a)
    while len(cs) % 2 == 0:
        cs = checksum(cs)
        print(len(cs))
    print(cs)
    
def extend(a):
    b = ''
    for c in reversed(a):
        if c == '0':
            b += '1'
        else:
            b += '0'
    
    return a + '0' + b

def checksum(b):
    cs = ''
    pairs = [b[i:i+2] for i in range(0, len(b), 2)]
    
    for p in pairs:
        if p[0] == p[1]:
            cs += '1'
        else:
            cs += '0'
    return cs

if __name__ == '__main__':
    main()