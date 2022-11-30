# 프로그래머스 - 프린터
# 스택/큐
def solution(priorities, location):
    p_lst = []
    lst = []
    cnt = 0

    for idx, p in enumerate(priorities):
        p_lst.append(p)
        lst.append([idx, p])
    p_lst.sort()

    while lst:
        if lst[0][1] == p_lst[-1]:
            cnt += 1
            if lst[0][0] == location:
                return cnt
            del lst[0]
            p_lst.pop()
        else:
            tmp = lst[0]
            del lst[0]
            lst.append(tmp)

    return 0