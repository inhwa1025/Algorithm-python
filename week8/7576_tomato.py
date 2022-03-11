# 백준 7576번 토마토
# 그래프, 너비 우선 탐색(BFS)
import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
date = [[-1 for _ in range(m)] for _ in range(n)]
max_date = 0
queue = deque()
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1 and date[i][j] == -1:
            queue.append((i, j))
            date[i][j] = 0

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and not tomato[nx][ny] and date[nx][ny] == -1:
            queue.append((nx, ny))
            tomato[nx][ny] = 1
            date[nx][ny] = date[x][y] + 1
            max_date = max(max_date, date[nx][ny])

for row in tomato:
    if 0 in row:
        print(-1)
        exit(0)

print(max_date)
