# 백준 1920번 수 찾기
# 자료 구조, 이분 탐색
import sys


def binary_search(num, data):    # O(log(N))
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if num == data[mid]:
            print(1)
            return 1
        elif num < data[mid]:
            end = mid - 1
        else:
            start = mid + 1

    print(0)
    return 0


def solution():
    n = int(input())
    a_list = list(map(int, sys.stdin.readline().split()))
    a_list.sort()       # O(log(N))
    m = int(input())
    check = list(map(int, sys.stdin.readline().split()))

    for chk in check:   # # O(Nlog(N))
        binary_search(chk, a_list)


solution()