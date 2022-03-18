# 백준 9084번 호텔
# 동적계획법, 배낭 문제
import sys

test = int(input())

for _ in range(test):
    n = int(input())
    pennies = list(map(int, sys.stdin.readline().split()))
    m = int(input())
    cache = [1] + [0] * m

    for penny in pennies:
        for i in range(m + 1):
            if penny <= i:
                cache[i] += cache[i - penny]

    print(cache[m])
