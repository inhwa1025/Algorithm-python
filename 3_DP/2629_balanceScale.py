# 백준 2629번 양팔저울
# 동적계획법, 배낭 문제
import sys
from itertools import combinations

weight_n = int(input())
weights = list(map(int, sys.stdin.readline().split()))
ball_n = int(input())
balls = list(map(int, sys.stdin.readline().split()))

subset = []
for i in range(1, weight_n+1):
    tmp = list(combinations(weights, i))
    for t in tmp:
        subset.append(sum(t))

tmp = list(combinations(subset, 2))
for a, b in tmp:
    subset.append(b - a)

for j in range(ball_n):
    if balls[j] in subset:
        print("Y", end=" ")
    else:
        print("N", end=" ")
