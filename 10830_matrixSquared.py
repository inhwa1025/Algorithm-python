import sys

size, b = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(size)]


def squared(p, before):
    if p == 2:
        after = [[0 for _ in range(size)] for _ in range(size)]
        for i in range(size):
            for j in range(size):
                for k in range(size):
                    after[i][j] += before[i][k] * matrix[k][j]
                after[i][j] %= 1000
        return after
    else:
        while p > 2:
            after = squared(2, before)
            return squared(p-1, after)


result = squared(b, matrix)
for m in range(size):
    for n in range(size):
        print(result[m][n], end=" ")
    print()
