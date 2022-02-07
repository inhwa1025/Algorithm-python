# 백준 13246번 행렬 제곱의 합
# 분할 정복을 이용한 거듭제곱, 수학
import sys

size, b = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(size)]
result = [[0] * size for _ in range(size)]


def squared(matrix1, matrix2):
    after = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                after[i][j] += matrix1[i][k] * matrix2[k][j]
            after[i][j] %= 1000
    return after


if b == 1:
    for i in range(size):
        for j in range(size):
            matrix[i][j] %= 1000
    for row in matrix:
        print(*row)
    exit(0)
else:
    tmp_matrix = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            result[i][j] += matrix[i][j]
            tmp_matrix[i][j] += matrix[i][j]

    for _ in range(b-1):
        tmp_matrix = squared(tmp_matrix, matrix)
        for i in range(size):
            for j in range(size):
                result[i][j] = (result[i][j] + tmp_matrix[i][j]) % 1000


for row in result:
    print(*row)
