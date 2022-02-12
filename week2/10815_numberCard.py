# 백준 10815번 숫자 카드
# 이진 탐색
import sys

n = int(input())
card = list(map(int, sys.stdin.readline().split()))
m = int(input())
guess = list(map(int, sys.stdin.readline().split()))

card.sort()


def check(guess_num):
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2

        if card[mid] == guess_num:
            return 1
        elif card[mid] > guess_num:
            end = mid - 1
        else:
            start = mid + 1
    return 0


for i in guess:
    print(check(i), end=' ')
