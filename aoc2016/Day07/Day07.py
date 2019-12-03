import re

def main():
    with open('Day07_Input.txt') as file:
        contents = [l.rstrip() for l in file.readlines()]
    
    total = 0
    for line in contents:
        if check_line(line):
            total += 1
    print(total)
    
def check_line(line):
    SSL_out = []
    SSL_in = []
    bracket = False
    for i in range(2, len(line)):
        if line[i] == '[':
            bracket = True
        elif line[i] == ']':
            bracket = False
        if line[i] == line[i-2] and line[i] != line[i-1] and not bracket:
            SSL_out.append(line[i] + line[i-1] + line[i])
            SSL_in.append(line[i-1] + line[i] + line[i-1])
         
    works = False   
    for i in range(len(SSL_out)):
        if SSL_in[i] in line:
            works = True
    if not works:
        return False
    else:
        hypernet = [s for s in re.split(r'\[|\]', line) if re.split(r'\[|\]', line).index(s) % 2 == 1]
        for s in hypernet:
            for SSL in SSL_in:
                if SSL in s:
                    return True
    return False
    
if __name__ == '__main__':
    main()