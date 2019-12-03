def main():
    with open('Day09_Input.txt') as file:
        contents = file.read()
    
    part2(contents)
    
def part1(contents):
    index = 0
    while index < len(contents):
        if contents[index] == '(' and is_marker(index, contents):
            m = 1
            while contents[index+m] != ')':
                m += 1
            nums = [int(n) for n in contents[index+1:index+m].split('x')]
            sub = contents[index+m+1:index+m+1+nums[0]]
            contents = contents[:index] + (nums[1] * sub) + contents[index+m+1+nums[0]:]
            index += (nums[1] * nums[0])
        else:
            index += 1
    print(len(contents))
    
def part2(contents):
    index = 0
    length = 0
    while index < len(contents):
        if contents[index] == '(' and is_marker(index, contents):
            m = 1
            while contents[index+m] != ')':
                m += 1
            nums = [int(n) for n in contents[index+1:index+m].split('x')]
            length += find_length(contents[index+m+1:index+m+1+nums[0]], nums)
            index += nums[0] + m + 1
        else:
            index += 1
            length += 1
    print(length)
        
def find_length(s, marker):
    if not '(' in s:
        return len(s * marker[1])
    else:
        total = 0
        while '(' in s:
            start = s.index('(')
            n = 1
            while s[start+n] != ')':
                n += 1
            nums = [int(n) for n in s[start+1:start+n].split('x')]
            total += find_length(s[start+n+1:start+n+1+nums[0]], nums) * marker[1]
            s = s[start+n+1+nums[0]:]
        return total
        
    
def is_marker(i, contents):
    n = 1
    while contents[i+n] != ')':
        n += 1
    nums = contents[i+1:i+n].split('x')
    try:
        int(nums[0])
        int(nums[1])
        return True
    except ValueError:
        return False
    return False
    
if __name__ == '__main__':
    main()