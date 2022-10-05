def solution(board, skill):
    n = len(board)
    m = len(board[0])
    prefix = [[0 for _ in range(m)] for _ in range(n)]
    answer = 0

    for sk in skill:  # [type, r1, c1, r2, c2, degree]
        degree = sk[5]
        if sk[0] == 1:  # 1: 공격(내구도 감소)
            degree = -degree
        # else:           2: 회복(내구도 증가)

        prefix[sk[1]][sk[2]] += degree
        if sk[4] + 1 < m:
            prefix[sk[1]][sk[4] + 1] -= degree
        if sk[3] + 1 < n:
            prefix[sk[3] + 1][sk[2]] -= degree
        if sk[3] + 1 < n and sk[4] + 1 < m:
            prefix[sk[3] + 1][sk[4] + 1] += degree

    # 세로 방향으로 누적합 계산
    for i in range(1, n):
        for j in range(m):
            prefix[i][j] += prefix[i - 1][j]

    # 가로 방향으로 누적합 계산
    for i in range(n):
        for j in range(1, m):
            prefix[i][j] += prefix[i][j - 1]

    # board와 누적합 더하기
    for i in range(n):
        for j in range(m):
            board[i][j] += prefix[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer
