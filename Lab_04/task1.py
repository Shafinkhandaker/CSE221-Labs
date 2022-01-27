import heapq
f = open('input1.txt', 'r')
fp = open('output1.txt', 'w')


def dijkstra(graph, source, dest):

    (dist, vis) = ([1000] * (dest + 1), [False] * (dest + 1))
    dist[source] = 0

    q = []

    heapq.heappush(q, (dist[source], source))
    while len(q) != 0:
        (weight, u) = heapq.heappop(q)

        if u == n:
            fp.write(str(dist[u]))
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
                    heapq.heappush(q, (dist[v], v))


t = int(f.readline())
for i in range(t):
    input1 = f.readline()
    (n, m) = list(map(int, input1.split()))

    if n == 1:
        fp.write('0')
        fp.write('\n')
        continue
    elif m == 1:

        line = f.readline()
        (u, v, w) = list(map(str, line.split()))
        fp.write(w)
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
