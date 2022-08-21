def solution(k, num, links):
    answer = 0
    end = []
    start = [x for x in range(len(num))]

    for i in range(len(links)):
        left = links[i][0]
        right = links[i][1]
        if left == -1 and right == -1:
            end.append(i)
        else:
            if left != -1:
                links[left].append(i)
                if left in start:
                    start.remove(left)
                    links[left].append(num[left])
            if right != -1:
                links[right].append(i)
                if right in start:
                    start.remove(right)
                    links[right].append(num[right])

    links[start[0]].append(-1)
    links[start[0]].append(num[start[0]])

    for j in range(len(num)):
        nxt = links[j][2]

        while nxt != -1:
            links[nxt][3] += num[j]
            nxt = links[nxt][2]

    if k == 1:
        return links[start[0]][3]

    result = [start[0]]
    visited = []
    can = []
    can_idx = []
    while True:
        for st in result:
            if st not in visited:
                left = links[st][0]
                right = links[st][1]
                if left != -1:
                    can.append(links[left][3])
                    can_idx.append(left)
                if right != -1:
                    can.append(links[right][3])
                    can_idx.append(right)
                visited.append(st)

        if len(can) == k:
            break

        m = max(can)
        node = can_idx[can.index(m)]
        can.remove(m)
        can_idx.remove(node)
        parent = links[node][2]
        links[parent][3] -= m
        result.append(node)


    answer = max(can)

    return answer


# ------------------------------------------
k = 4
num = [6, 9, 7, 5]
links = [[-1, -1], [-1, -1], [-1, 0], [2, 1]]
print(solution(k, num, links))
