# 백준 1092번 배
# 정렬, 그리디 알고리즘
import sys

n = int(sys.stdin.readline().strip())
crane = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().strip())
box = list(map(int, sys.stdin.readline().split()))

if max(crane) < max(box):
    print(-1)
    exit(0)

crane.sort(reverse=True)
box.sort()
time = 0

while True:
    time += 1
    for i in range(n):
        if not box:
            print(time)
            exit(0)
        if crane[i] < box[-1]: break
        box.pop()
