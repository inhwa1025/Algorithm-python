def solution(s):
    n = len(s)
    answer = n

    for i in range(1, n):
        p = 0
        comp = ""
        while p < n:
            slices = s[p:p + i]
            p += i
            cnt = 1
            while True:
                if s[p:p + i] == slices:
                    cnt += 1
                    p += i
                else:
                    break

            if cnt == 1:
                comp += slices
            else:
                comp += str(cnt) + slices

        if len(comp) < answer:
            answer = len(comp)

    return answer