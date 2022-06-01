# 1주차 연습문제 1번 - 완주하지 못한 선수
# 정렬

def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(participant) - 1):
        if participant[i] != completion[i]:
            return participant[i]

    return participant[-1]