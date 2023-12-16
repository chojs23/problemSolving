# BFS
import collections

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def solution(maps):
    answer = 0
    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
    cnt_map = []

    lever = (0, 0)
    exit = (0, 0)
    for r in range(len(maps)):
        for c in range(len(maps[0])):
            if maps[r][c] == "L":
                lever = (r, c)
            elif maps[r][c] == "E":
                exit = (r, c)
    print(exit, lever)

    for r in range(len(maps)):
        for c in range(len(maps[0])):
            if maps[r][c] == "S":
                cnt_map = bfs(r, c, maps, visited)
                break

    if cnt_map[exit[0]][exit[1]] == 0:
        return -1

    if cnt_map[lever[0]][lever[1]] == 0:
        return -1

    lever_cnt = cnt_map[lever[0]][lever[1]]

    visited = [[0] * len(maps[0]) for _ in range(len(maps))]

    for r in range(len(maps)):
        for c in range(len(maps[0])):
            if maps[r][c] == "L":
                cnt_map = bfs(r, c, maps, visited)
                break
    print(cnt_map)

    return cnt_map[exit[0]][exit[1]] + lever_cnt


def bfs(s_r, s_c, maps, visited):
    q = collections.deque()
    q.append((s_r, s_c))

    cnt_map = [[0] * len(maps[0]) for _ in range(len(maps))]

    visited[s_r][s_c] = 1
    cnt = -1
    while q:
        cnt += 1
        for t in range(len(q)):
            r, c = q.popleft()
            cnt_map[r][c] = cnt
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if (
                    0 <= nr < len(maps)
                    and 0 <= nc < len(maps[0])
                    and not visited[nr][nc]
                    and maps[nr][nc] != "X"
                ):
                    q.append((nr, nc))
                    visited[nr][nc] = 1

    return cnt_map


solution(["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"])
