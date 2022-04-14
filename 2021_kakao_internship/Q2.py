from collections import deque

visited = [[False for _ in range(5)] for _ in range(5)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(place, x, y):
    queue = deque()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < 5) and (0 <= ny < 5) and not visited[nx][ny]:
            visited[nx][ny] = True
            if place[nx][ny] == "P":
                return False
            elif place[nx][ny] == "O":
                queue.append((nx, ny))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < 5) and (0 <= ny < 5) and not visited[nx][ny] and place[nx][ny] == "P":
                return False

    return True


def solv(place):
    global visited
    visited = [[False for _ in range(5)] for _ in range(5)]

    for i in range(5):
        line = place[i]
        for j in range(5):
            if line[j] == "P":
                visited[i][j] = True
                if not bfs(place, i, j):
                    return 0
    return 1


def solution(places):
    answer = []

    for place in places:
        answer.append(solv(place))

    return answer
