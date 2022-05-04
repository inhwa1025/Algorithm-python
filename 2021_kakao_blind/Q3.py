def solution(info, query):
    answer = []
    applicant = []
    lan_list = [[] for _ in range(3)]  # cpp, java, python
    job_list = [[] for _ in range(2)]  # backend, frontend
    career_list = [[] for _ in range(2)]  # junior, senior
    food_list = [[] for _ in range(2)]  # chicken, pizza
    score = []

    for i in range(len(info)):
        tmp = list(info[i].split())
        applicant.append(tmp)
        # 언어 분류 (lan_list)
        if tmp[0] == 'cpp':
            lan_list[0].append(i)
        elif tmp[0] == 'java':
            lan_list[1].append(i)
        else:
            lan_list[2].append(i)
        # 직군 분류 (job_list)
        if tmp[1] == 'backend':
            job_list[0].append(i)
        else:
            job_list[1].append(i)
        # 경력 분류 (career_list)
        if tmp[2] == 'junior':
            career_list[0].append(i)
        else:
            career_list[1].append(i)
        # 소울 푸드 분류 (food_list)
        if tmp[3] == 'chicken':
            food_list[0].append(i)
        else:
            food_list[1].append(i)
        # 점수 분류 (score)
        score.append(int(tmp[4]))

    for q in query:
        tmp = list(q.split())

        filt = set([x for x in range(0, len(info))])

        # 개발 언어 필터링
        if tmp[0] == 'cpp':
            filt = filt & set(lan_list[0])
        elif tmp[0] == 'java':
            filt = filt & set(lan_list[1])
        elif tmp[0] == 'python':
            filt = filt & set(lan_list[2])

        # 직군 필터링
        if tmp[2] == 'backend':
            filt = filt & set(job_list[0])
        elif tmp[2] == 'frontend':
            filt = filt & set(job_list[1])

        # 경력 필터링
        if tmp[4] == 'junior':
            filt = filt & set(career_list[0])
        elif tmp[4] == 'senior':
            filt = filt & set(career_list[1])

        # 소울푸드 필터링
        if tmp[6] == 'chicken':
            filt = filt & set(food_list[0])
        elif tmp[6] == 'pizza':
            filt = filt & set(food_list[1])

        # 점수 필터링
        cnt = 0
        baseline = int(tmp[-1])
        for each in list(filt):
            if score[each] >= baseline:
                cnt += 1

        answer.append(cnt)

    return answer