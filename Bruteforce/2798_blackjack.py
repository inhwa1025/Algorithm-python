# 백준 2798번 블랙잭
# 브루트포스 알고리즘
from itertools import combinations
import sys

n, m = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

comb = list(combinations(cards, 3))

result = 0
for c in comb:
    tmp = sum(c)
    if result < tmp <= m:
        result = tmp

print(result)
