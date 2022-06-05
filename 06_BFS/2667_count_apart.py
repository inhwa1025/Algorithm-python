# 백준 2667번 단지번호붙이기
# 그래프, 너비 우선 탐색(BFS), 깊이 우선 탐색(DFS)
import sys
from collections import deque

n = 0
graph = []
sizes = []
visited = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()


def bfs(x, y, now_size):
    global graph, sizes, visited, dx, dy

    visited[x][y] = True
    queue.append((x, y))
    visited[x][y] = True
    size = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
                size += 1

    sizes.append(size)


def solution():
    global n, graph, sizes, visited

    n = int(input())
    graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 and not visited[i][j]:
                cnt += 1
                bfs(i, j, 1)

    sizes.sort()
    print(cnt)
    for size in sizes:
        print(size)


solution()
