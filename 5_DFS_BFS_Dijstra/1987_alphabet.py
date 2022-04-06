import sys

r, c = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(r)]
result = 1
passed = []
# 좌 우 상 하
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, depth):
    global result
    result = max(depth, result)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < r) and (0 <= ny < c) and (board[nx][ny] not in passed):
            passed.append(board[nx][ny])
            dfs(nx, ny, depth+1)
            passed.pop()


passed.append(board[0][0])
dfs(0, 0, 1)
print(result)
