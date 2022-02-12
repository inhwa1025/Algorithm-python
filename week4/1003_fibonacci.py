# 백준 1003번 피보나치 함수
# 동적계획법
testcase_num = int(input())
testcase = [int(input()) for _ in range(testcase_num)]

cache_zero = [1, 0]
cache_one = [0, 1]


def fib_func(num):
    if len(cache_zero) > num:
        return [cache_zero[num], cache_one[num]]
    left = fib_func(num-1)
    right = fib_func(num-2)
    cache_zero.append(left[0] + right[0])
    cache_one.append(left[1] + right[1])
    return [cache_zero[num], cache_one[num]]


for n in testcase:
    result = fib_func(n)
    print(result[0], result[1])
