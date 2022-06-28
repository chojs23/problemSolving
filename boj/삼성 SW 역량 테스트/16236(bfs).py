from copy import copy, deepcopy
from math import sqrt
from re import L
import sys
from collections import defaultdict, deque
from itertools import permutations
import heapq
import bisect

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

input = sys.stdin.readline
INF = sys.maxsize

# ===========================================================


n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]
sr, sc = 0, 0
fish_cnt = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            sr, sc = i, j
            board[i][j] = 2
        elif board[i][j] == 0:
            pass
        else:
            fish_cnt += 1

ans = 0

dr, dc = [-1, 0, 0, 1], [0, -1, 1, 0]
size = 2
eat_cnt = 0


def bfs(i, j):
    visited = [[0] * n for _ in range(n)]
    visited[i][j] = 1

    eat = []

    dist = [[0] * n for _ in range(n)]

    q = deque()
    q.append((i, j))

    while q:
        r, c = q.popleft()

        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == 0:
                if board[nr][nc] <= board[i][j] or board[nr][nc] == 0:
                    q.append((nr, nc))
                    visited[nr][nc] = 1
                    dist[nr][nc] = dist[r][c] + 1

                if board[nr][nc] < board[i][j] and board[nr][nc] != 0:
                    eat.append((nr, nc, dist[nr][nc]))

    if not eat:
        return -1, -1, -1
    eat.sort(key=lambda x: (x[2], x[0], x[1]))

    return eat[0][0], eat[0][1], eat[0][2]


while True:
    i, j = sr, sc
    er, ec, dist = bfs(i, j)
    if er == -1:
        break
    board[er][ec] = board[i][j]
    board[i][j] = 0
    sr, sc = er, ec

    eat_cnt += 1

    if eat_cnt == board[er][ec]:
        eat_cnt = 0
        board[er][ec] += 1
    ans += dist

print(ans)
