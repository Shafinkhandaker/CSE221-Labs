import heapq
f = open('input4.txt', 'r')
fp = open('output4.txt', 'w')


def network(graph, s, n):
    (dist, prev) = ([-9999] * (n + 1), [None] * (n + 1))
    q = []
    dist[s] = 9999

    heapq.heappush(q, (-dist[s], s))
    while len(q) != 0:
        (data, u) = heapq.heappop(q)
        data = -data

        alt = 0
        if u in graph:
            for a in graph[u]:
                (v, w) = a

                alt = min(dist[u], w)
                if alt > dist[v]:
                    dist[v] = alt
                    prev[v] = u
                    heapq.heappush(q, (-dist[v], v))

    for i in range(1, n + 1):
        if s == i:
            fp.write('0')
            fp.write(' ')
        elif dist[i] < 0:
            fp.write('-1')
            fp.write(' ')
        else:
            fp.write(str(dist[i]))
            fp.write(' ')
    fp.write('\n')


t = int(f.readline())
for i in range(t):
    input1 = f.readline()
    (n, m) = list(map(int, input1.split()))

    graph = {}
    for k in range(m):
        input2 = f.readline()
        (u, v, d) = list(map(int, input2.split()))

        if u not in graph:
            graph[u] = [(v, int(d))]
        else:

            list1 = graph[u]
            list1.append((v, int(d)))

    s = int(f.readline())

    if m == 0:
        if n == s:
            fp.write('0')
            fp.write('\n')
            continue
        else:
            fp.write('-1')
            fp.write('\n')
            continue

    network(graph, s, n)

f.close()
fp.close()
