def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    arr = [[] for _ in range(len(id_list))]

    for each_report in report:
        user, report_user = each_report.split()
        arr[id_list.index(report_user)].append(id_list.index(user))

    for report_user in arr:
        report_set = set(report_user)
        if len(report_set) >= k:
            for user in report_set:
                answer[user] += 1

    return answer