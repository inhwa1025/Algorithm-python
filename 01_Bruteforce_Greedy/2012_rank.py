# 백준 2012번 등수 매기기
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
