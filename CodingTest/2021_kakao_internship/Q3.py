def solution(n, k, cmd):
    answer = ''
    able = [i for i in range(n)]
    stack = []

    for now_cmd in cmd:
        if now_cmd == "C":
            stack.append((k, able[k]))

            del able[k]

            if k == len(able):
                k -= 1

        elif now_cmd == "Z":
            if stack:
                idx, col = stack.pop()
                able.insert(idx, col)
                if idx <= k:
                    k += 1

        elif now_cmd[0] == "U":
            x = int(now_cmd[2:])
            k -= x

        elif now_cmd[0] == "D":
            x = int(now_cmd[2:])
            k += x

    for i in range(n):
        if i in able:
            answer += "O"
        else:
            answer += "X"

    return answer


n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
cmd2 = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
print(solution(n, k, cmd))
print(solution(n, k, cmd2))