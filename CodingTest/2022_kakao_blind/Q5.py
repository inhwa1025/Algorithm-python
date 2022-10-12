# 양과 늑대, BFS, 백트래킹(중복 경로 체크 안함)
def solution(info, edges):
    # graph[i] = [자식의 노드 번호 리스트]
    graph = [[] for _ in range(len(info))]
    for edge in edges:
        graph[edge[0]].append(edge[1])
    visited = [False for _ in range(len(info))]
    global maxSheep
    maxSheep = 1

    # print(graph)

    def dfs(sheep, wolf, cur, path):
        global maxSheep
        # 현재 노드가 양이면 sheep += 1, 늑대이면 wolf += 1
        sheep += info[cur] ^ 1  # XOR 연산 사용 0^1=1
        wolf += info[cur]

        # print("경로:", path)
        # print("현재노드:", cur, ", maxSheep:", maxSheep, ", 현재 양/늑대:", sheep, ",", wolf)

        # 양이 늑대에게 잡아먹히는 경우 종료
        if sheep <= wolf:
            # print("end")
            return 0

        # 현재 양의 수와 최대값 비교
        maxSheep = max(maxSheep, sheep)

        # 가능한 모든 경우 탐색
        for p in path:
            for nxt in graph[p]:
                if not visited[nxt]:
                    path.append(nxt)
                    visited[nxt] = True
                    maxSheep = max(maxSheep, dfs(sheep, wolf, nxt, path))
                    visited[nxt] = False
                    path.pop()

        return maxSheep

    # 시작점은 루트노드
    visited[0] = True
    result = dfs(0, 0, 0, [0])

    return result
