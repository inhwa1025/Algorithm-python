# 백준 1202번 보석 도둑
# 자료 구조, 그리디 알고리즘, 정렬, 우선순위 큐
import sys
import heapq

jewel = []
bags = []
result = 0

n, k = map(int, sys.stdin.readline().split())

for _ in range(n):
    heapq.heappush(jewel, list(map(int, sys.stdin.readline().split())))

for _ in range(k):
    bags.append(int(sys.stdin.readline()))
bags.sort()

queue = []
for bag in bags:
    while jewel and jewel[0][0] <= bag:
        heapq.heappush(queue, -heapq.heappop(jewel)[1])
    if queue:
        result -= heapq.heappop(queue)
    elif not jewel:
        break

print(result)
