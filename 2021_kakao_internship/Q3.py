def solution(n, k, cmd):
    answer = ''
    table = ["O" for _ in range(n)]
    able = [i for i in range(n)]
    stack = []

    for now_cmd in cmd:
        if now_cmd == "C":
            table[able[k]] = "X"
            stack.append((k, able[k]))

            if k < len(able) - 1:
                k += 1
            else:
                k -= 1

        elif now_cmd == "Z":
            idx, col = stack.pop()
            able.insert(idx, col)
            table[col] = "O"

        elif now_cmd[0] == "U":
            x = int(now_cmd[2:])
            k -= x

        elif now_cmd[0] == "D":
            x = int(now_cmd[2:])
            k += x

    for result in table:
        answer += result

    return answer