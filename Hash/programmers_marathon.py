# 프로그래머스 - 완주하지 못한 선수
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


# 정렬을 사용해서 푼 방법
# 효율성: 34.96ms, 34.96ms, 74.36ms, 78.98ms, 75.82ms
def solution1(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(participant) - 1):
        if participant[i] != completion[i]:
            return participant[i]

    return participant[-1]
