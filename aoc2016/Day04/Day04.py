def main():
    with open('Day04_Input.txt') as file:
        contents = [name.rstrip() for name in file.readlines()]
        
    sum = 0
    for room in contents:
        num = int(room[-10:-7])
        
        letters = {}
        for l in room[:-10]:
            if not l in letters and not l == '-':
                letters[l] = 1
            elif not l == '-':
                letters[l] += 1
            
        if ''.join(most_common(letters)) == room[-6:-1]:
            sum += num
        
        if 'north' in rot_alpha(num % 26)(room[:-7]):
            print(rot_alpha(num % 26)(room[:-7]))
            
    print(sum)
        
def most_common(letters):
    top_five = []
    for _ in range(5):
        highest = 0
        highest_letter = 'z'
        for l in letters:
            if (letters[l] > highest and not l in top_five) or (letters[l] == highest and l <= highest_letter and not l in top_five):
                highest = letters[l]
                highest_letter = l
        top_five.append(highest_letter)
    
    return top_five

def rot_alpha(n):
    from string import ascii_lowercase as lc, ascii_uppercase as uc
    lookup = str.maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
    return lambda s: s.translate(lookup)
            
if __name__ == '__main__':
    main()