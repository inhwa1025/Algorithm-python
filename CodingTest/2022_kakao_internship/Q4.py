# 정확성 20/25
import heapq

INF = 1e9  # 양의 무한대


def solution(n, paths, gates, summits):
    answer = []
    queue = []
    m = len(paths)  # 경로 개수
    graph = [[] for _ in range(n + 1)]
    for path in paths:
        graph[path[0]].append((path[1], path[2]))
        graph[path[1]].append((path[0], path[2]))
    intensity = [INF for _ in range(n + 1)]  # 최소 intensity 저장
    min_result = INF
    min_top = INF

    for start in gates:  # 출입구 순회
        intensity = [INF for _ in range(n + 1)]  # 최소 intensity 저장
        intensity[start] = 0
        heapq.heappush(queue, (0, start, 0))  # 시작점 추가 (현재 instensity, 현재 위치, 봉우리)

        while queue:
            now_inst, now, top = heapq.heappop(queue)
            # print(now, top, now_inst)
            if intensity[now] != now_inst:
                continue
            if intensity[now] > min_result:
                continue
            elif intensity[now] == min_result and top >= min_top:
                continue
            if now in summits:
                if top and top != now:
                    continue
                else:
                    top = now
                    if intensity[now] == min_result and min_top > top:
                        min_top = top
                    elif intensity[now] < min_result:
                        min_top = top
                        min_result = intensity[now]
                    continue
            for nxt, nxt_inst in graph[now]:
                if nxt_inst > min_result:
                    continue
                if nxt_inst == min_result and top and top >= min_top:
                    continue
                if nxt == start:
                    intensity[nxt] = max(intensity[now], nxt_inst)
                    if top:
                        if intensity[nxt] == min_result and min_top > top:
                            min_top = top
                        elif intensity[nxt] < min_result:
                            min_top = top
                            min_result = min_result, intensity[nxt]
                    else:
                        continue
                if nxt != start and nxt in gates:
                    continue
                if intensity[nxt] <= max(intensity[now], nxt_inst):
                    if now == top:
                        if intensity[nxt] == min_result and min_top > top:
                            min_top = top
                        elif intensity[now] < min_result:
                            min_top = top
                            min_result = intensity[now]
                    continue

                intensity[nxt] = max(intensity[now], nxt_inst)
                heapq.heappush(queue, (intensity[nxt], nxt, top))

    answer = [min_top, min_result]

    return answer