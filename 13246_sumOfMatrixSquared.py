# 백준 13246번 행렬 제곱의 합
# 분할 정복을 이용한 거듭제곱, 수학
import sys

size, b = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(size)]


