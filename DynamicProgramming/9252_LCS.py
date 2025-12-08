# 9252번 최장 공통 부분 수열 찾기 (LCS, DP)
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

A = list(input())
B = list(input())
A.pop() # \n 제거
B.pop() # \n 제거

DP = [[0 for j in range(len(B)+1)] for i in range(len(A)+1)]
LCS = ""

for i in range(1, len(A)+1):
    for j in range(1, len(B)+1):
        if A[i-1] == B[j-1]:
            DP[i][j] = DP[i-1][j-1] + 1
        else:
            DP[i][j] = max(DP[i-1][j], DP[i][j-1])

print(DP[len(A)][len(B)])

# LCS 출력
def getLCS(r, c):
    if r == 0 or c == 0:
        return 
    if A[r-1] == B[c-1]:
        global LCS
        LCS = A[r-1] + LCS
        getLCS(r-1, c-1)
    else:
        if DP[r-1][c] > DP[r][c-1]:
            getLCS(r-1, c)
        else:
            getLCS(r, c-1)

getLCS(len(A), len(B))
print(LCS)
