# 백준 15661번 링크와 스타트
# 브루트포스
import sys
from itertools import combinations

n = int(input())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

sum_matrix = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n-1):
    for j in range(i+1, n):
        sum_matrix[i][j] = matrix[i][j] + matrix[j][i]


def function(sum_matrix):
    result = 2000
    for k in range(1, n//2+1):
        for l in combinations(range(n), k):
            group1 = [*l]
            group2 = list(set(range(n)) - set(group1))

            score1, score2 = 0, 0
            for part1 in combinations(group1, 2):
                score1 += sum_matrix[part1[0]][part1[1]]
            for part2 in combinations(group2, 2):
                score2 += sum_matrix[part2[0]][part2[1]]

            temp = abs(score1 - score2)

            if temp == 0:
                return 0
            elif temp < result:
                result = temp

    return result


print(function(sum_matrix))
