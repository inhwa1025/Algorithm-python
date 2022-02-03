import sys

size, b = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(size)]


def squared(matrix1, matrix2):
    after = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                after[i][j] += matrix1[i][k] * matrix2[k][j]
            after[i][j] %= 1000
    return after


def recursion(input_matrix, exponent):
    global matrix
    if exponent == 1:
        return input_matrix
    elif exponent%2 == 0:
        return squared(recursion(input_matrix, exponent//2), recursion(input_matrix, exponent//2))
    else:
        return squared(recursion(input_matrix, exponent-1), matrix)


result = recursion(matrix, b)

for m in range(size):
    for n in range(size):
        print(result[m][n], end=" ")
    print()
