import sys

size, b = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(size)]


def squared(before):
    global matrix
    after = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                after[i][j] += before[i][k] * matrix[k][j]
            after[i][j] %= 1000
    return after


result = matrix
for _ in range(b-1):
    result = squared(result)

for m in range(size):
    for n in range(size):
        print(result[m][n], end=" ")
    print()
