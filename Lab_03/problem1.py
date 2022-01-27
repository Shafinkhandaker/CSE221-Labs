file = open('input.txt', 'r')
node = int(file.readline())
edges = int(file.readline())
connections = []
for line in file:
    node1, node2 = line.split()
    node1 = int(node1)
    node2 = int(node2)
    connections.append([node1, node2])
file.close()


class Graph():
    def __init__(self, size):
        self.adj = [[] for i in range(size + 1)]

    def add_edge(self, v1, v2):
        self.adj[v1].append(v2)


graph = Graph(node)
for edge in connections:
    graph.add_edge(edge[0], edge[1])
