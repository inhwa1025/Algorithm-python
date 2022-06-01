def solution(n, lost, reserve):
    answer = n - len(lost)

    # 여벌 체육복을 가져온 학생이 도난을 당한 경우 먼저 처리
    for lost_st in lost:
        if lost_st in reserve:
            answer += 1
            reserve.remove(lost_st)
            lost.remove(lost_st)

    # 그 외
    for lost_st in lost:
        for res_st in reserve:
            if lost_st - 1 <= res_st <= lost_st + 1:
                answer += 1
                reserve.remove(res_st)
                break

    return answer