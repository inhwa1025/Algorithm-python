from itertools import combinations


# 채점 결과 정확성: 91.7/ 100.0
def solution_2(number, k):
    arr = list(number)

    maxidx = arr.index(max(arr[:k]))
    if maxidx > 0:
        k -= maxidx
        arr = arr[maxidx:]

    i = 0
    l = len(arr) - 1
    minval = min(arr)
    while k:
        if i > l:
            break
        elif arr[i] == minval or arr[i] < arr[i + 1]:
            arr.remove(arr[i])
            i -= 1
            k -= 1
            l -= 1
        else:
            i += 1

    return ''.join(arr)


# 시간초과
def solution_1(number, k):
    answer = list(combinations(list(number), len(number)-k))
    return ''.join(max(answer, reverse=True))
