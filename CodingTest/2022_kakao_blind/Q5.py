# 양과 늑대
from collections import deque


def solution(info, edges):
    # graph[i] = [자식의 노드 번호 리스트]
    graph = [deque() for _ in range(len(info))]
    for edge in edges:
        graph[edge[0]].append(edge[1])
    visited = [False for _ in range(len(info))]

    print(graph)

    stack = [0]  # 시작점은 루트노드
    result = 0  # 최대 양의 수
    shp_wolf = [0, 0]  # [현재 양의 수, 늑대의 수]
    while stack:
        top = stack.pop()
        if not visited[top]:
            shp_wolf[info[top]] += 1
            visited[top] = True
        print("현재노드:", top, end=" ")
        print(", result:", result, end=" ")
        print(", 현재 양/늑대:", shp_wolf)

        # 양이 늑대에게 잡아먹히는 순간 이전 노드로 돌아가기
        if shp_wolf[0] <= shp_wolf[1]:
            shp_wolf[info[top]] -= 1
            continue
        else:
            result = max(result, shp_wolf[0])

        # 더 이상 나아갈 노드가 없을 때
        if not graph[top]:
            if info[top]:  # 늑대일 때
                shp_wolf[info[top]] -= 1
            print("end")
            continue
        else:
            stack.append(top)
            stack.append(graph[top].popleft())

    return result