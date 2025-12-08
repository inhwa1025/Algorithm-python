# codility PassingCars - 부분합
# 정수 N개로 이루어진 배열 A. 0과 1로 이루어져있음. 0은 east, 1은 west
# passing car 카운트하기. 이동할 때 0<=P<Q<N, cars(P,Q) 의 두대의 마주보는 자동차쌍이 지나감 (N 은 1~100,000)
# 지나가는 차량의 쌍이 1,000,000,000 을 넘어가면 -1 반환
def solution(A):
    count = 0
    east_cars = 0
    for car in A:
        if car == 0:  # east로 가는 차
            east_cars += 1
        else:  # west로 가는 차
            if count >= 1000000000:
                return -1
            count += east_cars
    return count

# 시간복잡도 O(N**2) 으로 시간초과 발생
# def solution(A):
#     count = 0
#     for i in range(len(A)):
#         for j in range(i+1, len(A)):
#             if A[i] == 0 and A[j] == 1:
#                 count += 1
#                 if count > 1000000000:
#                     return -1
#     return count

print(solution([0, 1, 0, 1, 1]))
