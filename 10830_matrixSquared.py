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
    global size
    if exponent == 1:   # 왜 여기서 1000으로 나누기를 안해주면 틀렸다고 하는지 모르겠음..!
        for i in range(size):
            for j in range(size):
                input_matrix[i][j] %= 1000
        return input_matrix

    tmp_matrix = recursion(input_matrix, exponent//2)
    if exponent % 2:
        return squared(squared(tmp_matrix, tmp_matrix), input_matrix)
    else:
        return squared(tmp_matrix, tmp_matrix)


result = recursion(matrix, b)
for r in result:
    print(*r)
