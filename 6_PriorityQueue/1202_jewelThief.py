# 백준 1202번 보석 도둑
# 자료 구조, 그리디 알고리즘, 정렬, 우선순위 큐
import sys
import heapq

jewel = []
bag = []
result = 0

n, k = map(int, sys.stdin.readline().split())

for _ in range(n):
    weight, value = map(int, sys.stdin.readline().split())
    heapq.heappush(jewel, (-value, weight))

for _ in range(k):
    bag.append(int(sys.stdin.readline()))
bag.sort()

while jewel and bag:
    tmp = heapq.heappop(jewel)

    for i in range(len(bag)):
        if tmp[1] <= bag[i]:
            del bag[i]
            result += -tmp[0]
            break

print(result)
