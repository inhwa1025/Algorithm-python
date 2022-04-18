# 백준 1106번 호텔
# 동적계획법, 배낭 문제
import sys

c, n = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
cache = [0] + [sys.maxsize] * (c + 100)

for cost, customer in matrix:
    for i in range(customer, c + 101):
        cache[i] = min(cache[i], cache[i-customer] + cost)

print(min(cache[c:]))
