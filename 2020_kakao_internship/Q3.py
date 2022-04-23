def solv(gems):
    gem = set(gems)

    for i in range(len(gem), len(gems) + 1):

        for j in range(0, len(gems) - i + 1):
            if set(gems[j:j + i]) == gem:
                return [j + 1, j + i]


def solution(gems):
    answer = []

    answer = solv(gems)

    return answer