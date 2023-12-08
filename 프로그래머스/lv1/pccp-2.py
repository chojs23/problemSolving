# BFS

import collections


def solution(land):
    answer = 0

    for c in range(len(land[0])):
        answer = max(answer, bfs(land, 0, c))

    return answer


def bfs(land, i_r, i_c):
    dr = [0, 0, -1, 1]
    dc = [1, -1, 0, 0]
    q = collections.deque()

    max_r = len(land)
    max_c = len(land[0])

    last_r = 0

    visited = [[False] * max_c for _ in range(max_r)]

    result = 0

    q.append((i_r, i_c))
    while q:
        r, c = q.popleft()
        if visited[r][c]:
            continue

        if land[r][c] == 1:
            result += 1

        visited[r][c] = True

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if (
                land[r][c] == 1
                and 0 <= nr < max_r
                and 0 <= nc < max_c
                and land[nr][nc] == 1
                and not visited[nr][nc]
            ):
                q.append((nr, nc))
                if nc == i_c:
                    last_r = max(last_r, nr)

        if not r == max_r - 1:
            q.append((r + 1, i_c))

    return result


# test code
land = [
    [0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0],
    [1, 1, 0, 0, 0, 1, 1, 0],
    [1, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 1, 1],
]

print(solution(land))
