# 1주차 연습문제 1번 - 완주하지 못한 선수
# 해시

# 효율성: 24.31ms, 32.94ms, 32.94ms, 51.14ms, 62.41ms
def solution(participant, completion):
    dic = dict()
    for p in participant:
        dic[p] = dic.get(p, 0) + 1
    for c in completion:
        dic[c] -= 1
    result = [k for k, v in dic.items() if v > 0]

    return result[0]


# 효율성: 25.11ms, 31.30ms, 43.16ms, 54.96ms, 52.79ms
def solution1(participant, completion):
    dic = dict()
    for p in participant:
        dic[p] = dic.get(p, 0) + 1
    for c in completion:
        if dic[c] == 1:
            dic.pop(c)
            continue
        dic[c] -= 1

    return ''.join(dic.keys())
