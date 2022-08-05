# 백준 9663번 N-Queen
# 브루트포스, 백트래킹

n = int(input())
result = 0


# 퀸을 놓은 후 그 이후의 줄에 대해서만 불가능한 칸 체크
def visit(x, y, in_visited):
    tmp_visited = [visi[:] for visi in in_visited]
    for i in range(1, n-x):
        tmp_visited[x+i][y] = True  # 아래 방향 체크
        if 0 <= y-i < n:
            tmp_visited[x+i][y-i] = True    # 왼쪽 아래 대각선 체크
        if 0 <= y+i < n:
            tmp_visited[x+i][y+i] = True    # 오른쪽 아래 대각선 체크
    return tmp_visited


def recursion(q, _visited):     # q번째 줄에 퀸을 둘 수 있는 경우들을 확인하는 재귀함수
    global result
    # 한 줄에 퀸이 하나씩 들어가야 함
    # 한 줄 전체가 불가능한 경우 아예 n개의 퀸을 모두 놓을 수 없으므로 재귀 종료
    for idx in range(q, n):
        if sum(_visited[idx]) == n:
            return 0
    # 마지막 줄에 도달한 경우 가능한 모든 경우를 세고 재귀 종료
    if q == (n-1):
        result += n - sum(_visited[q])
        return 0

    for i in range(n):
        if not _visited[q][i]:   # 퀸을 둘 수 있는 경우
            tmp = visit(q, i, _visited)     # 퀸을 뒀을 때 불가능한 칸들 체크
            recursion(q+1, tmp)     # 그 다음 줄에 대해 재귀 호출
        # 재귀호출 종료 후 퀸을 둘 수 있는 다른 경우에 대해 체크


visited = [[False for _ in range(n)] for _ in range(n)]
recursion(0, visited)   # 0번째 줄부터 탐색 시작
print(result)
