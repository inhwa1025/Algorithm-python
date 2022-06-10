import heapq


def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)

    min1 = heapq.heappop(scoville)

    while scoville and min1 < K:
        min2 = heapq.heappop(scoville)
        heapq.heappush(scoville, min1 + min2 * 2)
        min1 = heapq.heappop(scoville)
        answer += 1

    if min1 < K:
        return -1

    return answer
