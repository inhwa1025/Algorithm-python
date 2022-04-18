# 백준 17829 222-풀링
# 분할 정복
import sys

size = int(input())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(size)]


def pooling(n, p_matrix):
    if n == 2:
        sort_matrix = sorted(sum(p_matrix, []))
        return sort_matrix[2]
    else:
        while n >= 4:
            result_matrix = []
            for i in range(0, n, 2):
                line = []
                for j in range(0, n, 2):
                    cur_matrix = [row[j:j+2] for row in p_matrix[i:i+2]]
                    line.append(pooling(2, cur_matrix))
                result_matrix.append(line)
            return pooling(n//2, result_matrix)


print(pooling(size, matrix))
