import sys
import hashlib
import random

def main():
    door_id = 'uqwqemis' 
    print('Password:', part1(door_id))
    
def part1(door_id):
    password = '________'
    pass_list = list(password)
    count = 0
    n = 4000000
    while '_' in password:
        input = door_id + str(n)
        hash = hashlib.md5(input.encode('utf-8')).hexdigest()
        if hash.startswith('00000'):
            pass_list[count] = hash[5]
            password = ''.join(pass_list)
            count += 1
        
        if n % 1000 == 0:
            for c in password:
                if c == '_':
                    sys.stdout.write(str(random.random())[-1])
                else:
                    sys.stdout.write(c)
            sys.stdout.write('\n')
        sys.stdout.flush()
        n += 1
    return password

def part2(door_id):
    password = '________'
    n = 0
    count = 0
    while count < 8:
        n += 1
        print(str(n) + ', ' + password)
        input = door_id + str(n)
        hash = hashlib.md5(input.encode('utf-8')).hexdigest()
        if hash.startswith('00000'):
            try:
                pass_list = list(password)
                if pass_list[int(hash[5])] == '_':
                    pass_list[int(hash[5])] = hash[6]
                    password = ''.join(pass_list)
                    count += 1
            except ValueError:
                continue
            except IndexError:
                continue
    return password
    
if __name__ == '__main__':
    main()