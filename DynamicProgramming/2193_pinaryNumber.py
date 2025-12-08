# 2193번 이친수 (DP)
import sys
input = sys.stdin.readline

N = int(input())
D = [[0,0] for _ in range(N+1)]
D[1] = [0,1]

for i in range(2, N+1):
    D[i][0] = D[i-1][0] + D[i-1][1]
    D[i][1] = D[i-1][0]

print(D[N][0] + D[N][1])
