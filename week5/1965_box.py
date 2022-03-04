# 백준 1965번 상자넣기
# 다이나믹 프로그래밍
import sys

n = int(input())
box = list(map(int, sys.stdin.readline().split()))

cache = [1 for _ in range(n)]


for i in range(1, n):
    for j in range(i):
        if box[i] > box[j]:
            cache[i] = max(cache[i], cache[j]+1)


print(max(cache))
