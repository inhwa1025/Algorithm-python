from itertools import combinations


def solution(orders, course):
    answer = []

    for course_n in course:
        c_dic = {}
        comb = []
        for i in range(len(orders)):
            comb += list(combinations(orders[i], course_n))

        if not comb:
            print("no")
            break

        for i in range(len(comb)):
            comb[i] = list(comb[i])
            comb[i].sort()
            comb[i] = ''.join(s for s in comb[i])

        for i in range(len(comb)):
            if comb[i] in c_dic:
                c_dic[comb[i]] += 1
            else:
                c_dic[comb[i]] = 1

        m = max(c_dic.values())
        if m < 2:
            break
        for set in c_dic.items():
            if set[1] == m:
                answer.append(set[0])

    answer.sort()

    return answer