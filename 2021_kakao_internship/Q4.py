import heapq


def solution(n, start, end, roads, traps):
    answer = 0
    INF = int(1e9)
    tr_active = [False for _ in range(n + 1)]
    graph = [[] for _ in range(n + 1)]
    r_graph = [[] for _ in range(n + 1)]
    distance = [INF for _ in range(n + 1)]
    queue = []

    for road in roads:
        graph[road[0]].append((road[1], road[2]))
        r_graph[road[1]].append((road[0], road[2]))

    distance[start] = 0
    heapq.heappush(queue, (0, start))

    while queue:
        now_dist, now = heapq.heappop(queue)

        if now == end: break
        if distance[now] != now_dist: continue

        if now in traps:
            tr_active[now] = not tr_active[now]

        for nxt, nxt_dist in graph[now]:
            if not tr_active[now] ^ tr_active[nxt]:
                distance[nxt] = distance[now] + nxt_dist
                heapq.heappush(queue, (distance[nxt], nxt))
        for nxt, nxt_dist in r_graph[now]:
            if tr_active[now] ^ tr_active[nxt]:
                distance[nxt] = distance[now] + nxt_dist
                heapq.heappush(queue, (distance[nxt], nxt))

    answer = distance[end]

    return answer