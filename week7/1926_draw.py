import sys
sys.setrecursionlimit(10000000)

height, width = map(int, sys.stdin.readline().split())
draw = [list(map(int, sys.stdin.readline().split())) for _ in range(height)]

visited = [[False for _ in range(height)] for _ in range(height)]
size = []


def dfs(x, y, idx):
    visited[x][y] = True
    if y < width-1 and draw[x][y+1] == 1 and not visited[x][y+1]:
        size[idx] += 1
        dfs(x, y+1, idx)
    if y > 1 and draw[x][y-1] and not visited[x][y-1]:
        size[idx] += 1
        dfs(x, y-1, idx)
    if x < height-1 and draw[x+1][y] == 1 and not visited[x+1][y]:
        size[idx] += 1
        dfs(x+1, y, idx)
    if x > 1 and draw[x-1][y] and not visited[x-1][y]:
        size[idx] += 1
        dfs(x-1, y, idx)


for i in range(height):
    for j in range(width):
        if draw[i][j] == 1 and not visited[i][j]:
            size.append(1)
            dfs(i, j, len(size)-1)

print(len(size))
if len(size):
    print(max(size))
else:
    print(0)
