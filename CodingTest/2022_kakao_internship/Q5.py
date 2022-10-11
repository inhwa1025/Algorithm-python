# 정확성 10/10, 효율성 2/9

def shiftrow(table):
    return [table[-1]] + table[:-1]

def rotate(table):
    first_row = [table[1][0]] + table[0][:-1]
    last_row = table[-1][1:] + [table[-2][-1]]

    n = len(table)
    for i in range(n - 2):
        table[i+1][0] = table[i+2][0]
        table[-2-i][-1] = table[-3-i][-1]

    table[0] = first_row
    table[-1] = last_row

    return table


def solution(rc, operations):
    answer = rc

    for oper in operations:
        if oper == "ShiftRow":
            answer = shiftrow(answer)
        else:
            answer = rotate(answer)

    return answer