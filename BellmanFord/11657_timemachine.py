import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # 노드개수, 엣지개수
edges = [] # 엣지 정보 저장 리스트
distance = [sys.maxsize] * (N+1) # 거리 리스트

# 엣지 데이터 저장
for i in range(M):
    start, end, time = map(int, input().split())
    edges.append((start,end,time))

distance[1] = 0 # 시작점 초기화

for _ in range(N-1):
    for start,end,time in edges:
        if distance[start] != sys.maxsize and distance[end] > distance[start] + time :
            distance[end] = distance[start] + time

# 음수 사이클 여부 확인
myCycle = False
for start,end,time in edges:
    if distance[start] != sys.maxsize and distance[end] > distance[start] + time :
        myCycle = True

if not myCycle:
    for i in range(2, N+1):
        if distance[i] != sys.maxsize:
            print(distance[i])
        else:
            print(-1)
else:
    print(-1)