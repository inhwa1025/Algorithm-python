# 백준 1927번 최소 힙
# 자료 구조, 우선순위 큐
import sys
import heapq

queue = []
heapq.heapify(queue)

n = int(sys.stdin.readline())

for _ in range(n):
    x = int(sys.stdin.readline())
    if x:
        heapq.heappush(queue, x)
    else:
        if not queue:
            print("0")
        else:
            print(heapq.heappop(queue))
