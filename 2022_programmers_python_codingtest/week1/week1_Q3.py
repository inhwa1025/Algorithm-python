# 채점 결과 정확성: 60.0/ 100.0
def solution(numbers):
    answer = ''

    strnum = [str(num) for num in numbers]
    strnum.sort()
    # print(strnum)

    for i in range(len(strnum) - 1):
        now = strnum[i]
        nxt = strnum[i + 1]
        if now + nxt > nxt + now:
            # print(now+nxt, nxt+now)
            answer = nxt + answer
            strnum[i + 1] = now
        else:
            answer = now + answer

    answer = str(int(strnum[-1] + answer))

    return answer
