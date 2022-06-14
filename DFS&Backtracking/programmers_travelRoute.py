# 프로그래머스 - 여행경로
# DFS
from collections import defaultdict


# Stack과 DFS를 사용한 풀이
# 모든 testcase가 0.2ms 안으로 끝남
# 1. { 시작점: [도착점들] } 의 형태로 그래프 생성
# 2. 도착점들의 리스트를 역순 정렬 ⭐️
# 3. 알파벳 순서상 빠른 것이 우선시되기 때문!!
#   - 역순으로 정렬해줌으로써 백트래킹처럼 모든 방법을 탐색하지 않고도 원하는 답을 한번에 찾을 수 있다!
#   - 출발점은 항상 "ICN"이므로 스택에 먼저 넣어두기
# 4. DFS를 통해서 모든 노드를 순회 (스택이 빌 때까지 아래를 반복)
#   4-1. 스택에서 가장 위에 저장된 데이터 top 꺼내오기
#   4-2. 만약 top이 그래프에 없거나, top을 시작점으로 하는 티켓이 없는 경우 path에 저장
#   4-3. 2번이 아니라면, top을 시작점으로 하는 도착점 리스트에서 pop 해와 스택에 저장
# 5. path에 저장된 값들을 거꾸로 뒤집어서 return
def solution(tickets):
    path = []

    # 1. 그래프 생성 -> {시작점: [도착점리스트]}
    graph = defaultdict(list)
    for (start, end) in tickets:
        graph[start].append(end)

    # 2. 도착점 리스트를 역순 정렬
    for airport in graph.keys():
        graph[airport].sort(reverse=True)

    # 3. 출발지는 항상 ICN이므로 stack에 먼저 넣어두기
    stack = ["ICN"]
    # 4. DFS로 모든 노드 순회
    while stack:
        # 4-1. 스택에서 가장 위의 저장된 데이터 꺼내오기
        top = stack.pop()

        # 4-2. top이 그래프에 없거나, top을 시작점으로 하는 티켓이 없는 경우 path에 저장
        if top not in graph or not graph[top]:
            path.append(top)
        # 4-3. top을 다시 스택에 넣고 top의 도착점 중 가장 마지막 지점을 꺼내와 스택에 저장
        else:
            stack.append(top)
            stack.append(graph[top].pop())

    # 5. path를 뒤집어서 반환
    return path[::-1]


# DFS와 백트래킹을 사용한 풀이
# testcase 중 하나가 154ms 이상 걸림
def solution1(tickets):
    visited = defaultdict(list)
    graph = defaultdict(list)
    start = "ICN"
    goal = len(tickets) + 1
    answer = []

    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])
        visited[ticket[0]].append(False)

    def dfs(now, path):
        nonlocal goal

        if len(path) == goal:
            answer.append(path)
            return 0
        for j in range(len(graph[now])):
            if not visited[now][j]:
                nxt = graph[now][j]
                visited[now][j] = True
                dfs(nxt, path + [nxt])
                visited[now][j] = False

    for i in range(len(graph[start])):
        airport = graph[start][i]
        visited[start][i] = True
        dfs(airport, [start, airport])
        visited[start][i] = False

    answer.sort()
    return answer[0]
