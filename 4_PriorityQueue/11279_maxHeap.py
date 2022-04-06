# 백준 11279번 최대 힙
# 자료 구조, 우선순위 큐
import sys
import heapq

queue = []
heapq.heapify(queue)

n = int(sys.stdin.readline())

for _ in range(n):
    x = int(sys.stdin.readline())

    if x:
        heapq.heappush(queue, -x)
    else:
        if queue:
            print(-heapq.heappop(queue))
        else:
            print("0")
