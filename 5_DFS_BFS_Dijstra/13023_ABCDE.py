import sys

n, m = map(int, sys.stdin.readline().split())
relation = [[] for _ in range(n)]
visited = [False for _ in range(n)]
result = False

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    relation[a].append(b)
    relation[b].append(a)


def dfs(this, depth):
    global result
    visited[this] = True

    if depth >= 4:
        result = True
        return
    if result:
        return

    for node in relation[this]:
        if not visited[node]:
            dfs(node, depth+1)
            visited[node] = False


for i in range(n):
    dfs(i, 0)
    visited[i] = False
    if result:
        break

print(1 if result else 0)
