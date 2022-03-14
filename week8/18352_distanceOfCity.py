# 백준 18352번 특정 거리의 도시 찾기
# 그래프, 너비 우선 탐색(BFS), 다익스트라
import sys
import heapq
INF = 1e9

n, m, k, x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
distance = [INF for _ in range(n+1)]
for _ in range(m):
    start, stop = map(int, sys.stdin.readline().split())
    graph[start].append(stop)
queue = []
distance[x] = 0
heapq.heappush(queue, (0, x))

while queue:
    now_dist, now = heapq.heappop(queue)
    if distance[now] != now_dist:
        continue
    for nxt in graph[now]:
        if distance[nxt] <= distance[now] + 1:
            continue
        distance[nxt] = distance[now] + 1
        heapq.heappush(queue, (distance[nxt], nxt))

if k in distance:
    result = []
    for i in range(n+1):
        if distance[i] == k:
            result.append(i)
    result.sort()
    for res in result:
        print(res)
else:
    print(-1)
