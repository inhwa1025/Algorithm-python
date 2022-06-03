# 채점 결과 정확성: 100.0/ 100.0
def solution(numbers):
    strnum = [str(num) for num in numbers]
    strnum.sort(key=lambda x: x * 3, reverse=True)

    return str(int(''.join(strnum)))


# 채점 결과 정확성: 60.0/ 100.0
def solution_1(numbers):
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
