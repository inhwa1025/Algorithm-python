# 백준 1002번 터렛
# 수학, 기하학
import sys
import math


def solution(x1, y1, r1, x2, y2, r2):
    # 원이 완전히 겹치는 경우: 접점 무한대
    if x1 == x2 and y1 == y2 and r1 == r2:
        return -1

    distance = math.sqrt(abs(x1-x2)**2 + abs(y1-y2)**2)

    if distance + r1 < r2 or distance + r2 < r1:  # 한 원이 다른 원 안에 있는 경우
        return 0
    elif distance + r1 == r2 or distance + r2 == r1:    # 한 원이 다른 원 안에서 내접
        return 1
    elif distance > r1 + r2:      # 한 원이 다른 원 안에 있지 않고 접점이 없는 경우
        return 0
    elif distance == r1 + r2:   # 두 원이 하나의 접점을 가지는 경우
        return 1
    else:   # 두 원이 두 개의 접점을 가지는 경우
        return 2


n = int(input())

for _ in range(n):
    _x1, _y1, _r1, _x2, _y2, _r2 = map(int, sys.stdin.readline().split())
    print(solution(_x1, _y1, _r1, _x2, _y2, _r2))
