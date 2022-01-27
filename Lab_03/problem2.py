from problem1 import graph, node
file = open('output_problem2.txt', 'w')


def bfs(visited, graph, node, endPoint):
    queue = []
    visited[node] = 1
    queue.append(node)
    while len(queue):
        m = queue.pop(0)
        file.write(f'{m} ')
        if m == endPoint:
            return
        for neighbour in graph.adj[m]:
            if visited[neighbour] == 0:
                visited[neighbour] = 1
                queue.append(neighbour)


visited = [0 for i in range(node+1)]
bfs(visited, graph, 1, 12)
file.close()
