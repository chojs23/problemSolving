# BFS
import collections

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def solution(maps):
    answer = []

    new_maps = [[0] * len(maps[0]) for _ in range(len(maps))]

    for r in range(len(maps)):
        for c in range(len(maps[0])):
            if maps[r][c] == "X":
                new_maps[r][c] = 0
            else:
                new_maps[r][c] = int(maps[r][c])

    visited = [[0] * len(new_maps[0]) for _ in range(len(new_maps))]
    for r in range(len(new_maps)):
        for c in range(len(new_maps[0])):
            if new_maps[r][c] != 0 and not visited[r][c]:
                answer.append(bfs(r, c, new_maps, visited))

    print(answer)
    return sorted(answer) if answer else [-1]


def bfs(s_r, s_c, maps, visited):
    q = collections.deque()
    q.append((s_r, s_c))
    visited[s_r][s_c] = 1
    cnt = 0

    while q:
        r, c = q.popleft()
        cnt += maps[r][c]

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if (
                0 <= nr < len(maps)
                and 0 <= nc < len(maps[0])
                and not visited[nr][nc]
                and maps[nr][nc] != 0
            ):
                q.append((nr, nc))
                visited[nr][nc] = 1

    return cnt
