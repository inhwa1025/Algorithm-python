# 백준 1535번 안녕
# 배낭 문제, 브루트포스 알고리즘, 다이나믹 프로그래밍
life = 100
joy = 0

n = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))


def recursion(i, cur_joy, cur_life):
    global joy

    if cur_life <= 0:
        pre_joy = cur_joy - J[i - 1]
        if pre_joy > joy:
            joy = pre_joy
        return joy

    if i == n:
        if cur_joy > joy:
            joy = cur_joy
        return joy

    recursion(i + 1, cur_joy + J[i], cur_life - L[i])
    recursion(i + 1, cur_joy, cur_life)


recursion(0, 0, life)
print(joy)
