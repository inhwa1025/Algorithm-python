# 백준 1717번 집합의 표현
# 자료 구조, 분리 집합
import sys

n, m = map(int, sys.stdin.readline().split())
lst = []
for i in range(n+1):
    lst.append([i])

for _ in range(m):
    opt, a, b = map(int, sys.stdin.readline().split())

    if opt == 0:
        idx = []
        for i in range(len(lst)):
            if a in lst[i] or b in lst[i]:
                idx.append(i)
        if len(idx) > 1:
            lst[idx[0]].extend(lst[idx[1]])
            del lst[idx[1]]
    else:
        result = False
        for i in range(len(lst)):
            if a in lst[i] and b in lst[i]:
                result = True
                break
        if result:
            print("YES")
        else:
            print("NO")

    # print(lst)
