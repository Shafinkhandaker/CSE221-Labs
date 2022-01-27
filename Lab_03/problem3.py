from problem1 import graph, node
file = open('output_problem3.txt', 'w')


def dfs_visit(graph, node, endPoint, visited):
    visited[node] = 1
    file.write(f"{node} ")
    if node == endPoint:
        return
    for neighbour in graph.adj[node]:
        if visited[endPoint] == 1:
            return
        if visited[neighbour] == False:
            dfs_visit(graph, neighbour, endPoint, visited)


visited = [0 for i in range(node+1)]
dfs_visit(graph, 1, 12, visited)
file.close()
