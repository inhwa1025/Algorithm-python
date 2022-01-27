# 백준 2448 별 찍기 -11
# 분할 정복, 재귀
size = int(input())

graph = [[" ", " ", "*", " ", " "], [" ", "*", " ", "*", " "], ["*", "*", "*", "*", "*"]]


def star(n, before):
    if len(before) == n:
        return before
    else:
        while len(before) < n:
            after = [[] for _ in range(len(before)*2)]
            for i in range(len(before)):
                after[i] = [" " * len(before)] + before[i] + [" " * len(before)]
                after[i + len(before)] = before[i] + [" "] + before[i]
            return star(n, after)


result = star(size, graph)
for r in result:
    print("".join(r))
