# 백준 13424번 비밀 모임
# 그래프, 다익스트라, 플로이드–와샬
import sys
import heapq
INF = 1e9

t = int(input())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n+1)]    # graph[now] = (nxt, nxt_dist)
    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    k = int(input())
    now_room = list(map(int, sys.stdin.readline().split()))
    distance = [[INF for _ in range(n+1)] for _ in range(k)]

    for i in range(k):
        distance[i][now_room[i]] = 0
        queue = []
        heapq.heappush(queue, (0, now_room[i]))
        while queue:
            now_dist, now = heapq.heappop(queue)
            if distance[i][now] != now_dist:
                continue
            for nxt, nxt_dist in graph[now]:
                if distance[i][nxt] <= distance[i][now] + nxt_dist:
                    continue
                distance[i][nxt] = distance[i][now] + nxt_dist
                heapq.heappush(queue, (distance[i][nxt], nxt))

    result = [INF]
    for room in range(1, n+1):
        tmp = 0
        for friend in range(k):
            tmp += distance[friend][room]
        result.append(tmp)

    print(result.index(min(result)))
