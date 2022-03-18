# 백준 1629번 곱셈
# 분할 정복을 이용한 거듭제곱
import sys

a, b, c = map(int, sys.stdin.readline().split())


def recursion(base, expo):
    global c
    if expo == 1:
        return base % c
    elif expo == 2:
        return base * base % c

    temp = recursion(base, expo // 2) % c
    if expo % 2 == 0:
        return recursion(temp, 2)
    else:
        return recursion(temp, 2) * base % c


print(recursion(a, b))
