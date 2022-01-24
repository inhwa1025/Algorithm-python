# 백준 1992번 쿼드트리
# 분할 정복, 재귀
import sys

n = int(input())
image = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]


def press(x, y, n):
    pixel = image[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if pixel != image[i][j]:
                print("(", end='')
                press(x, y, n//2)
                press(x, y+n//2, n//2)
                press(x+n//2, y, n//2)
                press(x+n//2, y+n//2, n//2)
                print(")", end='')
                return
    print(pixel, end='')


press(0, 0, n)
