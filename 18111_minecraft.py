# 백준 18111번 마인크래프트
# 구현, 브루트포스 알고리즘
import sys
from collections import Counter

n, m, invt = map(int, sys.stdin.readline().split())
ground = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
height, time = 0, 100000000000000

min_h = min(map(min, ground))
max_h = max(map(max, ground))
ground = dict

def leveling(hegiht):
    if hegiht

for i in range(min_h, max_h+1):

