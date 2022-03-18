# 백준 1041번 주사위
# 수학, 그리디 알고리즘
import sys

n = int(sys.stdin.readline().strip())
dice = list(map(int, sys.stdin.readline().split()))

if n == 1:
    print(sum(dice)-max(dice))
    exit(0)

fcf = sorted([min(dice[0], dice[5]), min(dice[1], dice[4]), min(dice[2], dice[3])], reverse=True)
two = fcf.pop() + fcf.pop()
three =two + fcf.pop()

print(three*4 + two*(8*n-12) + min(dice)*((n-2)*(n-2)+(n-2)*(n-1)*4))
