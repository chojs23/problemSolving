from copy import copy, deepcopy
from math import sqrt
import sys
from collections import defaultdict, deque
from itertools import permutations
import heapq

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

input = sys.stdin.readline
INF = sys.maxsize

# ===========================================================


n, m = map(int, input().split())

board = []

for i in range(n):
    board.append(list(map(int, input().rstrip())))

q = deque()

board2 = [[0] * m for _ in range(n)]

p = 0

visited = [[0] * m for _ in range(n)]


def bfs(r, c):
    global p
    tmp = []
    tmp.append((r, c))
    q.append((r, c))
    cnt = 1

    while q:
        r, c = q.popleft()
        visited[r][c] = 1
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if (
                0 <= nr < n
                and 0 <= nc < m
                and board[nr][nc] == 0
                and not visited[nr][nc]
                and board2[nr][nc] == 0
            ):
                visited[nr][nc] = 1
                q.append((nr, nc))
                tmp.append((nr, nc))
                cnt += 1
    for i in tmp:
        r, c = i
        board2[r][c] = (cnt, p)
    p += 1


point = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 0 and board2[i][j] == 0:
            bfs(i, j)
        else:
            point.append((i, j))

for x in point:
    i, j = x
    if board[i][j] == 1:
        pile = []
        for k in range(4):
            nr, nc = i + dr[k], j + dc[k]
            if (
                0 <= nr < n
                and 0 <= nc < m
                and board2[nr][nc] != 0
                and board2[nr][nc][1] not in pile
            ):
                board[i][j] += board2[nr][nc][0]
                pile.append(board2[nr][nc][1])


for i in range(n):
    for j in range(m):
        print(board[i][j] % 10, end="")
    print()
