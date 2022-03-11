# 백준 2178번 미로 탐색
# 그래프, 너비 우선 탐색(BFS)
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
distance = [[-1 for _ in range(m)] for _ in range(n)]
queue = deque()
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]


def bfs(x, y):
    queue.append((x, y))
    distance[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] and distance[nx][ny] == -1:
                queue.append((nx, ny))
                distance[nx][ny] = distance[x][y] + 1


bfs(0, 0)
print(distance[n-1][m-1])
