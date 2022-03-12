from collections import deque


def solution(maps):
    answer = 100 * 100
    n, m = len(maps), len(maps[-1])
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]
    q = deque()
    q.append((0, 0))
    time = 0
    while q:
        lenq = len(q)
        time += 1
        for _ in range(lenq):
            x, y = q.popleft()

            if x == n - 1 and y == m - 1:
                answer = time

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if (
                    nx >= 0
                    and nx < n
                    and ny >= 0
                    and ny < m
                    and not visited[nx][ny]
                    and maps[nx][ny]
                ):
                    q.append((nx, ny))
                    visited[nx][ny] = 1

    return answer if answer < 100 * 100 else -1
