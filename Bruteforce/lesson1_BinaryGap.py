# Codility 1-1. BinaryGap
def solution(N):
    N = bin(N)
    result = 0

    tmp = 0
    for i in range(2, len(N)):
        if N[i] == '1':
            result = max(result, tmp)
            tmp = 0
        else:
            tmp += 1

    return result
