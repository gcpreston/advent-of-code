def main():
    with open('Day02_Input.txt') as file:
        instructions = [l.rstrip() for l in file.readlines()]
        
    keypad = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    coordinates = [1, 1]
    
    code = solve(keypad, instructions, coordinates)
    print('Part 1 code:', code)
    
    keypad = [[0, 0, 1, 0, 0],
              [0, 2, 3, 4, 0],
              [5, 6, 7, 8, 9],
              [0, 'A', 'B', 'C', 0],
              [0, 0, 'D', 0, 0]]
    coordinates = [2, 0]
    
    code = solve(keypad, instructions, coordinates)
    print('Part 2 code:', code)

def solve(keypad, instructions, coordinates):
    moves = {'U': [-1, 0], 'R': [0, 1], 'D': [1, 0], 'L': [0, -1]}
    code = ''
    
    for button in instructions:
        for move in button:
            next = [x + y for x, y in zip(coordinates, moves[move])]
            
            if 0 <= next[0] < len(keypad) and 0 <= next[1] < len(keypad[next[0]]) and not keypad[next[0]][next[1]] == 0:
                coordinates = list(next)
        
        code += str(keypad[coordinates[0]][coordinates[1]])
    return code

if __name__ =='__main__':
    main()