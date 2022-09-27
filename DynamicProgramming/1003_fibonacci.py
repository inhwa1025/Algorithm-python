# 백준 1003번 피보나치 함수
# 동적계획법
cache_zero = [1, 0]     # 0 출력 횟수
cache_one = [0, 1]      # 1 출력 횟수

testcase_num = int(input())
testcase = [int(input()) for _ in range(testcase_num)]


def fibonacci(k):
    if k >= len(cache_zero):
        zero1, one1 = fibonacci(k-1)
        zero2, one2 = fibonacci(k-2)
        cache_zero.append(zero1 + zero2)
        cache_one.append(one1 + one2)
    return cache_zero[k], cache_one[k]


for n in testcase:
    result_zero, result_one = fibonacci(n)
    print(result_zero, result_one)
