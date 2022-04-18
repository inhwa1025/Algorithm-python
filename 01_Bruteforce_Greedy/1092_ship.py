# 백준 1092번 배
# 정렬, 그리디 알고리즘
import sys

n = int(input())
crane = list(map(int, sys.stdin.readline().split()))
m = int(input())
box = list(map(int, sys.stdin.readline().split()))

crane.sort(reverse=True)
box.sort(reverse=True)
time = 0

if crane[0] < box[0]:
    print(-1)
    exit(0)

while box:
    time += 1
    for cur_crane in crane:
        for j in range(len(box)):
            if cur_crane >= box[j]:
                del box[j]
                break

print(time)
