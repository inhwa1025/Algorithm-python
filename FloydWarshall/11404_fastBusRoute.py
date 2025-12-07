# 시작 점 지정 없이 모든 경우의 최단거리 구하기
# 플로이드워셜 결과값은 2차원 리스트
import sys
input = sys.stdin.readline

N = int(input()) # 도시 개수
M = int(input()) # 노선 개수
# 2차원 리스트 초기화
distance = [[sys.maxsize for j in range(N+1)] for i in range(N+1)]
for i in range(1, N+1):
    distance[i][i] = 0 # 자기 자신은 0

for i in range(M):
    s, e, v = map(int, input().split())
    if distance[s][e] > v:
        distance[s][e] = v

# 플로이드워셜 알고리즘
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]

for i in range(1, N+1):
    for j in range(1, N+1):
        if distance[i][j] == sys.maxsize:
            print(0, end=' ')
        else:
            print(distance[i][j], end=' ')
    print()