import sys

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
location = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

cache = [[-1 for _ in range(n)] for _ in range(n)]
