def solv(gems):
    if len(gems) == 1:
        return [1, 1]

    gem = set(gems)
    gem_list = list(gem)
    min_idx = len(gems)
    max_idx = 0

    for i in range(len(gem_list)):
        cnt = gems.count(gem_list[i])
        if cnt == 1:
            min_idx = min(min_idx, gems.index(gem_list[i]))
            max_idx = max(max_idx, gems.index(gem_list[i]))

    if min_idx == 0 and max_idx == len(gems) - 1:
        return [1, max_idx + 1]
    elif set(gems[min_idx:max_idx + 1]) == gem:
        return [min_idx + 1, max_idx + 1]
    else:
        tmp_len = max_idx - min_idx + 1

        for i in range(max(tmp_len + 1, len(gem)), len(gems) + 1):
            tmp_min = max_idx - i + 1 if max_idx - i + 1 > 0 else 0
            tmp_max = min_idx + i - 1 if min_idx + i - 1 < len(gems) - 1 else len(gems) - 1

            for j in range(tmp_min, tmp_max - i + 1):
                if set(gems[j:j + i]) == gem:
                    return [j + 1, j + i]


def solution(gems):
    answer = []

    answer = solv(gems)

    return answer