from collections import defaultdict
from itertools import combinations
from bisect import bisect_left


def solution(infos, querys):
    answer = []
    info_dict = defaultdict(list)

    for info in infos:
        info = list(info.split())
        condition = info[:-1]
        score = int(info[-1])

        for i in range(5):
            combs = list(combinations(condition, i))

            for comb in combs:
                info_dict[''.join(comb)].append(score)

    for value in info_dict.values():
        value.sort()

    for query in querys:
        query = query.replace(' and ', '')
        query = query.replace('-', '')
        query = list(query.split())
        if len(query) == 1:
            query.append(query[0])
            query[0] = ''

        if query[0] in info_dict:
            scores = info_dict[query[0]]
            index = bisect_left(scores, int(query[1]))
            answer.append(len(scores) - index)
        else:
            answer.append(0)

    return answer