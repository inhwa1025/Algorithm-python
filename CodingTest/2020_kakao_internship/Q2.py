def mul(ex):
    while '*' in ex:
        idx = ex.index('*')
        mul = int(ex[idx - 1]) * int(ex[idx + 1])
        ex = ex[:idx - 1] + [mul] + ex[idx + 2:]

    return ex


def plus(ex):
    while '+' in ex:
        idx = ex.index('+')
        mul = int(ex[idx - 1]) + int(ex[idx + 1])
        ex = ex[:idx - 1] + [mul] + ex[idx + 2:]

    return ex


def minus(ex):
    while '-' in ex:
        idx = ex.index('-')
        mul = int(ex[idx - 1]) - int(ex[idx + 1])
        ex = ex[:idx - 1] + [mul] + ex[idx + 2:]

    return ex


def solution(expression):
    answer = 0

    ex = []
    result = []

    last = 0
    for i in range(len(expression)):
        if expression[i] in ["*", "+", "-"]:
            ex.append(expression[last:i])
            ex.append(expression[i])
            last = i + 1
    ex.append(expression[last:])
    del last

    tmp1 = mul(ex)
    result.append(abs(int(minus(plus(tmp1))[0])))
    result.append(abs(int(plus(minus(tmp1))[0])))

    tmp2 = plus(ex)
    result.append(abs(int(mul(minus(tmp2))[0])))
    result.append(abs(int(minus(mul(tmp2))[0])))

    tmp3 = minus(ex)
    result.append(abs(int(mul(plus(tmp3))[0])))
    result.append(abs(int(plus(mul(tmp3))[0])))

    answer = max(result)

    return answer