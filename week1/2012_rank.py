# 백준 18111번 마인크래프트
# 정렬, 그리디 알고리즘
import sys

n = int(sys.stdin.readline().strip())
predict = []
result = 0

for _ in range(n):
    predict.append(int(sys.stdin.readline().strip()))

predict.sort()

for i in range(n):
    result += abs(i+1-predict[i])

print(result)
