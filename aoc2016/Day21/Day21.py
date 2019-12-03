from itertools import permutations

def main():
    with open('Day21_Input.txt') as file:
        contents = [line.rstrip().split(' ') for line in file.readlines()]
    
    password = 'fbgdceah'
    
    unscramble(contents, password)

def scramble(contents, password):
    for line in contents:
        if line[0] == 'swap':
            if line[1] == 'position':
                password = swap_pos(password, int(line[2]), int(line[5]))
            else:
                password = swap_letters(password, line[2], line[5])
        elif line[0] == 'rotate':
            if line[1] == 'right':
                password = rotate_right(password, int(line[2]))
            elif line[1] == 'left':
                password = rotate_left(password, int(line[2]))
            else:
                if password.index(line[6]) >= 4:
                    password = rotate_right(password, 2 + int(password.index(line[6])))
                else:
                    password = rotate_right(password, 1 + int(password.index(line[6])))
        elif line[0] == 'reverse':
            password = reverse(password, int(line[2]), int(line[4]))
        else:
            password = move(password, int(line[2]), int(line[5]))
    
    return password

def unscramble(contents, password):
    for s in [''.join(p) for p in permutations(password)]:
        if scramble(contents, s) == password:
            print(s)
            break

def swap_pos(s, x, y):
    if x < y:
        lower = x
        higher = y
    else:
        lower = y
        higher = x
    return ''.join((s[:lower], s[higher], s[lower+1:higher], s[lower], s[higher+1:]))

def swap_letters(s, a, b):
    s = s.replace(a, '_')
    s = s.replace(b, a)
    s = s.replace('_', b)
    return s

def rotate_left(s, n):
    n = n % len(s)
    return s[n:] + s[:n]

def rotate_right(s, n):
    n = n % len(s)
    return s[-n:] + s[:-n]

def unrotate(s, a):
    for i in range(1, len(s) + 1):
        test_pass = rotate_left(s, i)
        if test_pass.index(a) >= 4:
            if s == rotate_right(test_pass, 2 + int(test_pass.index(a))):
                return test_pass
        else:
            if s == rotate_right(test_pass, 1 + int(test_pass.index(a))):
                return test_pass

def reverse(s, x, y):
    if x < y:
        lower = x
        higher = y
    else:
        lower = y
        higher = x
    return s[:lower] + s[lower:higher+1][::-1] + s[higher+1:]

def move(s, x, y):
    c = s[x]
    s = s[:x] + s[x+1:]
    s = s[:y] + c + s[y:]
    return s
    
if __name__ == '__main__':
    main()