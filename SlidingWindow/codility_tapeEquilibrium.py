# N개의 정수로 이루어진 배열 A
# 0<P<N , sum(A[0~P-1])-sum(A[P~N]) 의 절대값중 최소값 구하기
import sys


def solution(A):
    result = sys.maxsize
    left = 0
    right = sum(A)
    for a in A[:-1]:
        left += a
        right -= a
        result = min(result, abs(left-right))
    return result
