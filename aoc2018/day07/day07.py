import re
from al60.data.graphs import DirectedGraph


def main():
    p = re.compile(r'Step (\S) must be finished before step (\S) can begin.')
    with open('input.txt') as file:
        edges = []
        for line in file.readlines():
            m = p.match(line.strip())
            edges.append((m.group(1), m.group(2)))

    g = DirectedGraph()
    added = set()

    for u, v in edges:
        if u not in added:
            g.add_node(u)
            added.add(u)
        if v not in added:
            g.add_node(v)
            added.add(v)

        g.add_edge(u, v)

    print('Part 1:', part1(g))
    print('Part 2:', part2(g))


def part1(g: DirectedGraph):
    return ''.join(g.topological_sort())


def part2(g: DirectedGraph, n=5):
    # TODO: Implement using library dfs
    clock = 0
    # subtract 64 for character value and add 60 flat gives -4
    tasks = {v: ord(v) - 4 for v in g.nodes()}
    # how many remaining prerequesites does each task have?
    in_degrees = {v: len(g.in_edges(v)) for v in g.nodes()}
    to_be_removed = []

    def assign_workers():
        while len(workers) < n and queue:
            workers.append(
                queue.pop(min((queue[i], i) for i in range(len(queue)))[1]))

    queue = [v for v in g.nodes() if len(g.in_edges(v)) == 0]
    workers = []
    assign_workers()

    while workers:
        for u in workers:
            tasks[u] -= 1

            if tasks[u] == 0:
                to_be_removed.append(u)

                for _, v in g.out_edges(u):
                    in_degrees[v] -= 1

                    # check if all prerequisites have been completed
                    if in_degrees[v] == 0:
                        queue.append(v)

        # remove from workers while not iterating over list to avoid bugs
        while to_be_removed:
            workers.remove(to_be_removed.pop())

        # re-populate workers
        assign_workers()

        clock += 1

    return clock


if __name__ == '__main__':
    main()
