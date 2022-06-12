# 프로그래머스 - 체육복
# 그리디
def solution(n, lost, reserve):
    # 여벌 체육복을 가져온 학생이 도난을 당한 경우 먼저 처리
    reserve_uniq = list(set(reserve) - set(lost))
    lost_uniq = list(set(lost) - set(reserve))

    # 그 외
    for res_st in reserve_uniq:
        if res_st - 1 in lost_uniq:
            lost_uniq.remove(res_st - 1)
        elif res_st + 1 in lost_uniq:
            lost_uniq.remove(res_st + 1)

    return n - len(lost_uniq)