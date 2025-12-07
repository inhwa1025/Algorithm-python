import sys
from queue import PriorityQueue
input = sys.stdin.readline

V,E = map(int, input().split()) # 노드개수, 엣지개수
K = int(input()) # 출발노드
distance = [sys.maxsize] * (V+1) # 거리 저장 리스트
visited = [False] * (V+1) # 방문 여부 저장 리스트
myList = [[] for _ in range(V+1)] # 엣지 데이터 저장 인접 리스트
q = PriorityQueue() # 다익스트라 우선 순위 큐

for _ in range(E): # 인접리스트에 엣지 정보 저장
    u,v,w = map(int, input().split())
    myList[u].append((v,w))

# 출발 노드 설정
q.put((0, K))
distance[K] = 0

while q.qsize() > 0: # 큐가 빌 때 까지
    current = q.get()
    c_v = current[1]
    if visited[c_v]: # 방문한 적 있으면 넘어가기
        continue
    visited[c_v] = True
    for tmp in myList[c_v]: # 현재 선택 노드의 엣지
        next = tmp[0]
        value = tmp[1]
        if distance[next] > distance[c_v] + value:
            distance[next] = distance[c_v] + value
            q.put((distance[next], next))

for i in range(1, V+1):
    if visited[i]:
        print(distance[i])
    else:
        print("INF")

