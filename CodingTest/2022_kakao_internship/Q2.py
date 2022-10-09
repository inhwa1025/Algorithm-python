from collections import deque

result = []


def recursion(q1, q2, s1, s2, cnt):
    print(s1, s2, cnt)

    if s1 == s2:
        result.append(cnt)
    if len(q1) < 1 or len(q2) < 1:
        result.append(-1)

    x = q1.popleft()
    q2.append(x)
    s1 -= x
    s2 += x
    cnt += 1

    recursion(q1, q2, s1, s2, cnt)
    recursion(q2, q1, s2, s1, cnt)
    q2.popleft()
    q1.append(x)


def solution(queue1, queue2):
    answer = -2
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    recursion(queue1, queue2, sum1, sum2, 0)
    recursion(queue2, queue1, sum2, sum1, 0)
    print(result)

    return answer