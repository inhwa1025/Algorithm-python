import math


def isPrime(number):
    if number in [0, 1]:
        return False

    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True


def baseChange(n, k):
    if k == 10:
        return str(n)

    result = ""
    while n > 0:
        result = str(n % k) + result
        n = n // k

    return result


def solution(n, k):
    answer = 0
    changed = baseChange(n, k)
    start = 0
    end = 0
    length = len(changed)

    for i in range(length):
        if changed[i] == '0':
            end = i
            if isPrime(int(changed[start:end])):
                answer += 1
            start = end

    if changed[length - 1] != '0':
        if isPrime(int(changed[start:length])):
            answer += 1

    return answer
