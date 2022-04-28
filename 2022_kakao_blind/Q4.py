apeach_info = []
candidate = [0 for _ in range(11)]
max_differ = 0


def selectbest(result):
    global candidate
    for i in range(len(result)):
        if candidate[10 - i] > result[10 - i]:
            break
        elif result[10 - i] > candidate[10 - i]:
            candidate = result[:]
            break


def recursion(i, cur_n, ryan, apeach, result):
    global candidate
    global max_differ
    global apeach_info

    if cur_n < 0 or i > 10 or apeach < 0:
        return 0
    elif cur_n == 0 or i == 10:
        result[10] = cur_n
        cur_n = 0
        differ = ryan - apeach
        if differ > max_differ:
            candidate = result[:]
            max_differ = differ
        elif differ == max_differ:
            selectbest(result)
        return 0
    else:
        next_result = result[:]
        recursion(i + 1, cur_n, ryan, apeach, next_result)

        next_result[i] = apeach_info[i] + 1
        next_n = cur_n - apeach_info[i] - 1
        next_ryan = ryan + 10 - i
        next_apeach = (apeach - 10 + i) if apeach_info[i] else apeach

        recursion(i + 1, next_n, next_ryan, next_apeach, next_result)


def solution(n, info):
    global candidate
    global max_differ
    global apeach_info
    apeach_info = info

    answer = []

    if info[0] == n:
        return [-1]

    apeach = 0
    for i in range(len(info)):
        if info[i]:
            apeach += (10 - i)

    recursion(0, n, 0, apeach, [0 for _ in range(11)])

    if max_differ > 0:
        answer = candidate
    else:
        return [-1]

    return answer
