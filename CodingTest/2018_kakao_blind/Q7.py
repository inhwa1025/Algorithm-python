def solution(lines):  # '날짜 응답완료시간 처리시간'
    answer = 0
    logs = []

    def time_to_msec(time):  # hh:mm:ss.sss
        hh = float(time[0:2])
        mm = float(time[3:5])
        ss = float(time[6:])
        return int(hh * 60 * 60 * 1000 + mm * 60 * 1000 + ss * 1000)

    def throughput(start, end):
        cnt = 0
        for l in logs:
            if l[0] < end and l[1] >= start:
                cnt += 1
        return cnt

    for line in lines:
        end = time_to_msec(line[11:23])
        tat = float(line[24:-1]) * 1000 - 1
        start = end - tat if end - tat >= 0 else 0
        logs.append((start, end))

    for log in logs:
        print(log)
        answer = max(answer, throughput(log[0], log[0] + 1000), throughput(log[1], log[1] + 1000))

    return answer