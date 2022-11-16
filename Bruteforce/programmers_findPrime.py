# 프로그래머스 - 카펫
# 완전탐색
from math import sqrt
from itertools import permutations


def is_prime_number(x):
    if x in [0, 1]:
        return False  # 소수가 아님
    # 2부터 x의 제곱근까지 모든 수를 확인하며
    for i in range(2, int(sqrt(x)) + 1):
        # x가 해당 수로 나누어 떨어진다면
        if x % i == 0:
            return False  # 소수가 아님
    return True  # 소수임


def solution(numbers):
    prime = set()
    n = len(numbers)

    for i in range(1, n + 1):
        tmp = list(map(''.join, permutations(numbers, i)))
        # print("tmp:",tmp)
        for each in tmp:
            each = int(each)
            if is_prime_number(each):
                prime.add(each)
                # print(prime)

    answer = len(prime)
    return answer
