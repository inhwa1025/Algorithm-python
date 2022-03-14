# 백준 10282번 해킹
# 그래프, 다익스트라
import sys
import heapq
INF = 1e9

test = int(input())

for _ in range(test):
    n, d, c = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n+1)]    # graph[now] = (nxt, nxt_dist)
    for _ in range(d):
        a, b, s = map(int, sys.stdin.readline().split())
        graph[b].append((a, s))
    queue = []
    distance = [INF for _ in range(n+1)]
    distance[c] = 0
    heapq.heappush(queue, (0, c))

    while queue:
        now_dist, now = heapq.heappop(queue)
        if distance[now] != now_dist:
            continue
        for nxt, nxt_dist in graph[now]:
            if distance[nxt] <= distance[now] + nxt_dist:
                continue
            distance[nxt] = distance[now] + nxt_dist
            heapq.heappush(queue, (distance[nxt], nxt))

    result = []
    for dist in distance:
        if dist < INF:
            result.append(dist)
    print(len(result), end=" ")
    print(max(result))
