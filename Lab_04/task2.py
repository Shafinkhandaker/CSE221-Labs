import heapq
f = open('input2.txt', 'r')
fp = open('output2.txt', 'w')


def dijkstra(graph, source, dest):

    (dist, prev, vis) = ([1000] * (dest + 1), [None] * (dest + 1),
                         [False] * (dest + 1))
    dist[source] = 0

    q = []

    heapq.heappush(q, (dist[source], source))
    while len(q) != 0:
        (weight, u) = heapq.heappop(q)

        if u == n:

            list1 = []
            (p, q) = (0, n)
            while prev[q] != None:
                p = prev[q]
                list1.append(p)
                q = p

            for i in range(len(list1) - 1, -1, -1):
                fp.write(str(list1[i]))
                fp.write(' ')
            fp.write(str(n))
            break

        if vis[u]:
            continue
        vis[u] = True

        alt = 0
        if u in graph:
            for a in graph[u]:
                (v, w) = a
                alt = dist[u] + w

                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
                    heapq.heappush(q, (dist[v], v))


t = int(f.readline())
for i in range(t):
    input1 = f.readline()
    (n, m) = list(map(int, input1.split()))

    if n == 1:
        fp.write(str(n))
        fp.write('\n')
        continue
    elif m == 1:

        line = f.readline()
        (u, v, w) = list(map(str, line.split()))
        fp.write(u)
        fp.write(' ')
        fp.write(v)
        fp.write('\n')
        continue
    else:

        graph = {}
        for k in range(m):
            input2 = f.readline()

            (u, v, w) = list(map(int, input2.split()))
            if u not in graph:
                graph[u] = [(v, int(w))]
            else:

                list1 = graph[u]
                list1.append((v, int(w)))

        dijkstra(graph, 1, n)

f.close()
fp.close()
