# codility MaxCounters
# 0으로 초기화된 N 카운터. 2가지 operation 가능
# increase(X) : counter X를 1 증가
# max counter : 모든 카운터를 카운터 중 최대값으로 설정
# M개의 정수로 이루어진 A 배열
# A[K] = X 일 때, (1 <= X <= N) increase(X) 연산 수행
# A[K] = N+1 일 때, max counter 연산 수행
# max 값을 배열 내에서 매번 찾으면 시간복잡도가 10만**2이므로 시간초과 발생. 별도의 변수로 관리


# 시간복잡도 계산:
# 1. counter = [0] * N           # O(N)
# 2. for a in A: (M = len(A))    # O(M)
#    - if a == N+1: counter = [max_counter]*N   # O(N) (최악: A 안에 N+1이 많을 때 여러 번 O(N))
# 전체 시간복잡도는 O(N + M * N) = O(MN)
#
# maxcounter 연산 개선:
# - counter 전체를 매번 갱신하지 않고, 마지막 max counter가 발생한 값을 기록해뒀다가,
#   실제로 counter를 읽거나 쓸 때(=increase 연산 시)만 그 값을 반영하도록 함 (lazy update 방식)
# - 즉, counter를 한 번에 모두 갱신하는 대신, maxcounter 발생시 기준값만 갱신하여,
#   실제 갱신은 필요할 때만 부분적으로 수행 --> O(M + N) 가능
def solution(N, A):
    counter = [0] * N
    max_counter = 0
    now_max = 0
    for a in A:
        if a <= N:
            if counter[a-1] < max_counter: # lazy update
                counter[a-1] = max_counter
            counter[a-1] += 1
            now_max = max(now_max, counter[a-1])
        else:
            max_counter = now_max
    for i in range(N):
        if counter[i] < max_counter:
            counter[i] = max_counter
    return counter

print(solution(5, [3, 4, 4, 6, 1, 4, 4]))
