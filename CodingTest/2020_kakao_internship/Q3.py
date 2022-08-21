def solution(gems):
    gem_num = len(set(gems))
    dic = {gems[0]: 1}
    start, end = 0, 0
    result = [0, len(gems) - 1]

    while 0 <= start < len(gems) and 0 <= end < len(gems):
        if len(dic) == gem_num:
            if end - start < result[1] - result[0]:
                result = [start, end]
            if dic[gems[start]] == 1:
                del dic[gems[start]]
            else:
                dic[gems[start]] -= 1
            start += 1
        else:
            if end == len(gems) - 1:
                break
            end += 1
            if gems[end] in dic.keys():
                dic[gems[end]] += 1
            else:
                dic[gems[end]] = 1

    return [result[0] + 1, result[1] + 1]