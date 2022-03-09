# 백준 1926번 그림
# 그래프, 너비 우선 탐색(BFS), 깊이 우선 탐색(DFS)
import sys
from collections import deque

height, width = map(int, sys.stdin.readline().split())
draw = [list(map(int, sys.stdin.readline().split())) for _ in range(height)]

visited = [[False for _ in range(width)] for _ in range(height)]
queue = deque()
cnt = 0
max_size = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    global max_size
    queue.append((x, y))
    visited[x][y] = True
    each_size = 1

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if (0 <= nx < height) and (0 <= ny < width) and draw[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
                each_size += 1

    max_size = max(max_size, each_size)


for i in range(height):
    for j in range(width):
        if draw[i][j] == 1 and not visited[i][j]:
            cnt += 1
            bfs(i, j)

print(cnt)
print(max_size)
