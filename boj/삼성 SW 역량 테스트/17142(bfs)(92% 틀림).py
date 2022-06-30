from copy import copy, deepcopy
from math import sqrt
from re import L
import sys
from collections import defaultdict, deque
from itertools import combinations, permutations
import heapq
import bisect

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

input = sys.stdin.readline
INF = sys.maxsize

# ===========================================================

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

v_pos = []
global_check = 1
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            v_pos.append([i, j])
        elif board[i][j] == 0:
            global_check = 0
if global_check:
    print(0)
    exit()

v_comb = list(combinations(v_pos, m))

ans = INF


def bfs(virus):
    ret = 0
    q = deque()
    visited = [[0] * n for _ in range(n)]
    for v in virus:
        q.append(v)
        visited[v[0]][v[1]] = 1

    while q:
        length = len(q)
        check = 0
        for _ in range(length):

            r, c = q.popleft()

            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]

                if (
                    0 <= nr < n
                    and 0 <= nc < n
                    and board[nr][nc] == 0
                    and not visited[nr][nc]
                ):
                    visited[nr][nc] = 1
                    q.append([nr, nc])
                    check = 1
                if (
                    0 <= nr < n
                    and 0 <= nc < n
                    and board[nr][nc] == 2
                    and not visited[nr][nc]
                ):
                    visited[nr][nc] = 1
                    q.append([nr, nc])
        if check:
            ret += 1

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                if board[i][j] == 0 or board[i][j] == 2:
                    return -100
    return ret


for comb in v_comb:
    ret = bfs(comb)
    if ret == -100:
        pass
    else:
        ans = min(ans, ret)
print(ans) if ans != INF else print(-1)
