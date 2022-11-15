# 프로그래머스 - 카펫
# 수학 (근의 공식 사용)
from math import sqrt


def solution(brown, yellow):
    # 가로+세로 = tmp
    tmp = int((brown+4)/2)
    # (가로-2)*(세로-2) = yellow
    # a+b=tmp, (a-2)*(b-2)=yellow, b=(tmp-a),
    # (a-2)*(tmp-2-a)=yellow, -a*a + tmp*a + (4-2*tmp) = yellow
    # a*a - tmp*a + yellow + 2*tmp - 4 = 0
    # 근의 공식: a = (tmp + sqrt(tmp**2-4*(yellow+2*tmp-4)))/2
    a = int((tmp + sqrt(tmp**2-4*(yellow+2*tmp-4)))/2)
    b = tmp - a
    # print(a, b)
    answer = [a, b]
    return answer
