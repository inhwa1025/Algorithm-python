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
    cur_num = dice[5-i]
    tmp_dice = dice[0:i] + dice[i+1:6]
    tmp_dice.remove(cur_num)
    cur_num += min(tmp_dice)
    if cur_num < two:
        two = cur_num
    tmp_dice.remove(min(tmp_dice))
    cur_num += min(tmp_dice)
    if cur_num < three:
        three = cur_num

print(three*4 + two*((n-2)*8+4) + min(dice)*((n-2)*(n-2)*5+(n-2)*4))
