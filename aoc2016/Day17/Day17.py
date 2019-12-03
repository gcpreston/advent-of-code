from hashlib import md5
from itertools import compress
import operator

def main():
    input = 'awrkjxxr'
    # input = 'ihgpwlah'
    # input = 'hijkl'
    
    global moves
    global directions
    moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    directions = ['U', 'D', 'L', 'R']
     
    print(bfs(input, (0, 0), (3, 3)))
    
def bfs(input, start, end):
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([start])
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        
        path_h = ''
        if len(path) > 1:
            for i in range(len(path) - 1):
                diff = (path[i+1][0] - path[i][0], path[i+1][1] - path[i][1])
                path_h += directions[moves.index(diff)]
        # get the last node from the path
        node = path[-1]
        # path found
        if node == end:
            return path_h
        
        doors = [False, False, False, False]
        hash = md5((input + path_h).encode('utf-8')).hexdigest()[:4]
        
        for i in range(len(hash)):
            if 98 <= ord(hash[i]) <= 102:
                doors[i] = True
        adjacents = list(compress(moves, doors))
        for i in range(len(adjacents)):
            adjacents[i] = tuple(map(operator.add, node, adjacents[i]))
        
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        for adjacent in adjacents:
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)
    
if __name__ == '__main__':
    main()