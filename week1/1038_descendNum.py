# 백준 1038번 감소하는 수
# 백트래킹, 브루트포스 알고리즘
import sys
from collections import deque

n = int(sys.stdin.readline().strip())

if n < 10:
    print(n)
    exit(0)
if n > 1022:
    print(-1)
    exit(0)

nums = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
count = 9

while nums:
    cur_num = nums.popleft()
    for i in range(10):
        if cur_num%10 <= i: break
        nums.append(cur_num*10 + i)
        count += 1
        if count == n:
            print(nums[-1])
            exit(0)
