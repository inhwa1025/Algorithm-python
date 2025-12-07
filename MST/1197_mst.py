import sys
from queue import PriorityQueue
input = sys.stdin.readline

N, M = map(int, input().split()) # 노드 수, 엣지 수
pq = PriorityQueue() # 엣지 정보 저장 우선순위 큐
parent = [0] * (N+1) # 대표 노드 저장 리스트 (유니온&파인드)

# 대표 노드 초기화
for i in range(N+1):
    parent[i] = i

# 우선순위 큐에 엣지 정보 저장. 자동 정렬됨
for i in range(M):
    s,e,w = map(int, input().split()) # 시작점, 끝점, 가중치
    pq.put((w,s,e)) # 가중치 기준 정렬

# 유니온&파인드
def find(a):
    if a == parent[a]:
        return a
    else: # 대표 노드 찾아가기
        parent[a] = find(parent[a]) # 경로압축
        return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b: # 사이클이 발생하지 않으므로 연결
        parent[b] = a

useEdge = 0
result = 0

while useEdge < N-1:
    w, s, e = pq.get()
    if find(s) != find(e):
        union(s, e)
        result += w
        useEdge += 1

print(result)