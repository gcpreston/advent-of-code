def main():
    favorite = 10
    dim = 50
    global building
    building = [[' ' for _ in range(dim)] for _ in range(dim)]
    
    for y in range(dim):
        for x in range(dim):
            num = bin((x*x + 3*x + 2*x*y + y + y*y) + favorite)
            ones = 0
            for c in num:
                if c == '1':
                    ones += 1
            if ones % 2 == 1:
                building[y][x] = '#'
            else:
                building[y][x] = '.'
    
    for r in range(len(building)):
        for c in range(len(building[0])):
            if r == 39 and c == 31:
                print('O', end='')
            else:
                print(building[r][c], end='')
        print()
        
    global graph
    graph = {}
    print(len(bfs(graph, (1, 1), (31, 39))) - 1)

def bfs(graph, start, end):
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([start])
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == end:
            return path
        # add adjacents to graph
        graph[node] = []
        if building[node[1]][node[0] + 1] == '.' and (node[0] + 1, node[1]) not in path:
            graph[node].append((node[0] + 1, node[1]))
        if building[node[1] + 1][node[0]] == '.' and (node[0], node[1] + 1) not in path:
            graph[node].append((node[0], node[1] + 1))
        if node[0] != 0 and building[node[1]][node[0] - 1] == '.' and (node[0] - 1, node[1]) not in path:
            graph[node].append((node[0] - 1, node[1]))
        if node[1] != 0 and building[node[1] - 1][node[0]] == '.' and (node[0], node[1] - 1) not in path:
            graph[node].append((node[0], node[1] - 1))
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)

if __name__ == '__main__':
    main()