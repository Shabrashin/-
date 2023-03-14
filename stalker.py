from math import inf
from collections import deque, defaultdict


def bfs(start, graph):
    d = deque()
    d.append(start)
    dist = {key: inf for key in graph}
    dist[start] = 0
    while d:
        cur = d.popleft()
        for to in graph[cur]:
            edge = int(to[1] == 0)
            if dist[to] > dist[cur] + edge:
                dist[to] = dist[cur] + edge
                if edge == 1:
                    d.append(to)
                else:
                    d.appendleft(to)
    return dist


with open('input.txt', 'r') as f:
    n, k = map(int, f.readline().split())
    graph = defaultdict(list)

    for lvl in range(1, k+1):
        r = int(f.readline())
        for _ in range(r):
            a, b = map(int, f.readline().split())
            graph.setdefault((a, lvl), []).append((b, lvl))   
            graph.setdefault((b, lvl), []).append((a, lvl))   
            
    for key in list(graph.keys()):
        zero_lvl = (key[0], 0)
        graph.setdefault(zero_lvl, []).append(key)
        graph.setdefault(key, []).append(zero_lvl)
    

res = bfs((1, 0), graph)
if res[(n, 0)] != inf:
    print(res[(n, 0)])
else:
    print(-1)
