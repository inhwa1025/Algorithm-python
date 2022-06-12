# 백준 14888번 연산자 끼워넣기
# 브루트포스, 백트래킹
import sys
max_result = -1e9
min_result = 1e9
n = 0
arr = []


def backtracking(idx, oper, result):
    global max_result, min_result

    if idx == n:
        if result > max_result:
            max_result = result
        if result < min_result:
            min_result = result
        return 0

    if oper[0] > 0:
        _oper = [oper[0]-1, oper[1], oper[2], oper[3]]
        backtracking(idx+1, _oper, result + arr[idx])

    if oper[1] > 0:
        _oper = [oper[0], oper[1]-1, oper[2], oper[3]]
        backtracking(idx + 1, _oper, result - arr[idx])

    if oper[2] > 0:
        _oper = [oper[0], oper[1], oper[2]-1, oper[3]]
        backtracking(idx + 1, _oper, result * arr[idx])

    if oper[3] > 0:
        _oper = [oper[0], oper[1], oper[2], oper[3]-1]
        if result < 0:
            backtracking(idx + 1, _oper, -(abs(result) // arr[idx]))
        else:
            backtracking(idx + 1, _oper, result // arr[idx])


def solution():
    global n, arr

    n = int(input())
    arr = list(map(int, sys.stdin.readline().split()))
    oper = list(map(int, sys.stdin.readline().split()))  # +, -, *, %

    backtracking(1, oper, arr[0])

    print(max_result)
    print(min_result)

    return 0


solution()
