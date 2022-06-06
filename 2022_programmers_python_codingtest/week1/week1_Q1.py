# 1주차 연습문제 1번 - 완주하지 못한 선수
# 정렬
# 효율성: 34.96ms, 34.96ms, 74.36ms, 78.98ms, 75.82ms

def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(participant) - 1):
        if participant[i] != completion[i]:
            return participant[i]

    return participant[-1]
