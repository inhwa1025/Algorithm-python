# 프로그래머스 - 디스크 컨트롤러
# 힙
import heapq


def solution(jobs):
    n = len(jobs)
    answer = 0
    now = 0
    jobs.sort(reverse=True)
    queue = []

    while jobs:
        if not queue:
            job = jobs.pop()
            heapq.heappush(queue, (job[1], job[0]))
        while queue:
            if jobs and now >= jobs[-1][0]:
                job = jobs.pop()
                heapq.heappush(queue, (job[1], job[0]))
            else:
                run, arrival = heapq.heappop(queue)
                now = now + run if now > arrival else arrival + run
                answer += now - arrival

    return answer // n
