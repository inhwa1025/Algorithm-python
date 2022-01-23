# 백준 1041번 주사위
# 수학, 그리디 알고리즘
import sys

n = int(sys.stdin.readline().strip())
dice = list(map(int, sys.stdin.readline().split()))

if n == 1:
    print(sum(dice)-max(dice))
    exit(0)

three = two = sum(dice)

for i in range(6):
    cur_sum = dice[5-i]
    tmp_dice = dice[0:i] + dice[i+1:6]
    tmp_dice.remove(cur_sum)
    cur_sum += min(tmp_dice)
    if cur_sum < two:
        two = cur_sum
    tmp_dice.remove(min(tmp_dice))
    cur_sum += min(tmp_dice)
    if cur_sum < three:
        three = cur_sum

print(three*4 + two*(8*n-12) + min(dice)*(5*n*n-16*n+12))
