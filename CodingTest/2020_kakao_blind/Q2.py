def slices(w):  # 문자열 분리
    left, right = 0, 0
    for i in range(len(w)):
        if w[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            return w[:i + 1], w[i + 1:]


def is_correct(u):  # 올바른 괄호 문자열인지 확인
    left, right = 0, 0
    for i in range(len(u)):
        if u[i] == '(':
            left += 1
        else:
            right += 1
        if right > left:
            return False
    if left == right:
        return True
    else:
        return False


def solution(p):
    answer = ''
    if len(p) == 0:  # 1. 입력이 빈 문자열인 경우
        return answer

    u, v = slices(p)  # 2. 두 균형잡힌 괄호 문자열 u, v로 분리

    if is_correct(u):  # 3. u가 올바른 괄호 문자열인 경우
        return u + solution(v)  # 3-1.
    else:  # 4. u가 올바른 괄호 문자열이 아닌 경우
        answer = '('  # 4-1
        answer += solution(v)  # 4-2
        answer += ')'  # 4-3

        u = u[1:-1]  # 4-4
        for each in u:
            if each == '(':
                answer += ')'
            else:
                answer += '('

        return answer  # 4-5
