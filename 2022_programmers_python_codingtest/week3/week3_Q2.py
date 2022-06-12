def solution(N, number):
    base = [0, N, N * 11, N * 111, N * 1111, N * 11111, N * 111111, N * 1111111, N * 11111111]
    arr = [[] for _ in range(9)]  # arr[i] = N을 i번 사용하여 얻을 수 있는 값들을 저장

    for i in range(1, 9):
        if number == base[i]:
            return i
        arr[i].append(base[i])

        # arr[i] = arr[1]과 arr[i-1]을 조합, arr[2]과 arr[i-2]을 조합, ..., arr[i-1]과 arr[1]을 조합
        for j in range(1, i):
            for a in arr[j]:
                for b in arr[i - j]:
                    tmp = [a + b, a - b, a * b, a // b]
                    for t in tmp:
                        if number == t:
                            return i
                        elif t > 0:
                            arr[i].append(t)

        arr[i] = set(arr[i])  # 중복 제거를 위해 set으로 변환

    return -1   # 8번 안에 답이 나오지 않으면 -1을 반환


print(solution(8, 53))
