import collections
import itertools
from copy import copy, deepcopy
import math
import sys
from collections import defaultdict, deque
from itertools import combinations, permutations
import heapq
import bisect
import math

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

input = sys.stdin.readline
INF = sys.maxsize

# ==========================================================

pdr, pdc = [-1, 1, 0, 0, -1, -1, 1, 1], [0, 0, -1, 1, -1, 1, -1, 1]


def getPossibleP(r, c):
    res = []
    for i in range(8):
        nr, nc = r + pdr[i], c + pdc[i]
        if 0 <= nr < N and 0 <= nc < N and board[nr][nc] != "0":
            res.append([nr, nc, 1])
    return res


bdr, bdc = [-1, -1, 1, 1], [-1, 1, -1, 1]


def getPossibleB(r, c):
    res = []
    for i in range(4):
        cnt = 1
        nr, nc = r + bdr[i], c + bdc[i]
        while 0 <= nr < N and 0 <= nc < N:

            if board[nr][nc] != "0":
                res.append([nr, nc, cnt])
                break

            nr, nc = nr + bdr[i], nc + bdc[i]
            cnt += 1
    return res


def getPossibleQ(r, c):
    res = []
    for i in range(8):
        cnt = 1
        nr, nc = r + pdr[i], c + pdc[i]
        while 0 <= nr < N and 0 <= nc < N:
            if board[nr][nc] != "0":
                res.append([nr, nc, cnt])
                break
            nr, nc = nr + pdr[i], nc + pdc[i]
            cnt += 1
    return res


ndr, ndc = [-1, -2, -2, -1, 1, 2, 2, 1], [-2, -1, 1, 2, -2, -1, 1, 2]


def getPossibleN(r, c):
    res = []
    for i in range(8):
        nr, nc = r + ndr[i], c + ndc[i]

        if 0 <= nr < N and 0 <= nc < N and board[nr][nc] != "0":
            res.append([nr, nc, 2])
    return res


def getPossibleR(r, c):
    res = []
    for i in range(4):
        cnt = 1
        nr, nc = r + pdr[i], c + pdc[i]
        while 0 <= nr < N and 0 <= nc < N:
            if board[nr][nc] != "0":
                res.append([nr, nc, cnt])
                break
            nr, nc = nr + pdr[i], nc + pdc[i]
            cnt += 1
    return res


N = int(input())
board = [list(input().split()) for _ in range(N)]
visited = [[(0, 0)] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if board[i][j] == "P":
            P = (i, j)
            possibleP = getPossibleP(i, j)
            board[i][j] = "0"

for i, r in enumerate(board):
    for j, c in enumerate(r):

        if c == "B":
            possibleB = getPossibleB(i, j)
        elif c == "Q":
            possibleQ = getPossibleQ(i, j)
        elif c == "N":
            possibleN = getPossibleN(i, j)
        elif c == "R":
            possibleR = getPossibleR(i, j)
        elif c == "K":
            K = (i, j)

board[P[0]][P[1]] = "P"


def bfs(start):
    q = deque()
    sr, sc = start
    q.append((sr, sc, 0))
    visited[sr][sc] = (1, 0)
    ans = INF
    while q:
        r, c, cost = q.popleft()

        if board[r][c] == "K":

            if visited[r][c][1] < ans:
                ans = visited[r][c][1]
            continue

        if board[r][c] == "P":
            for k in possibleP:
                nr, nc, cnt = k
                if not visited[nr][nc][0] or (visited[nr][nc][0] and visited[nr][nc][1] > cnt + cost):
                    visited[nr][nc] = (1, cnt + cost)
                    q.append((nr, nc, cost + cnt))

        elif board[r][c] == "B":
            for k in possibleB:
                nr, nc, cnt = k
                if not visited[nr][nc][0] or (visited[nr][nc][0] and visited[nr][nc][1] > cnt + cost):
                    visited[nr][nc] = (1, cnt + cost)
                    q.append((nr, nc, cost + cnt))
        elif board[r][c] == "Q":
            for k in possibleQ:
                nr, nc, cnt = k
                if not visited[nr][nc][0] or (visited[nr][nc][0] and visited[nr][nc][1] > cnt + cost):
                    visited[nr][nc] = (1, cnt + cost)
                    q.append((nr, nc, cost + cnt))

        elif board[r][c] == "N":
            for k in possibleN:
                nr, nc, cnt = k
                if not visited[nr][nc][0] or (visited[nr][nc][0] and visited[nr][nc][1] > cnt + cost):
                    visited[nr][nc] = (1, cnt + cost)
                    q.append((nr, nc, cost + cnt))

        elif board[r][c] == "R":
            for k in possibleR:
                nr, nc, cnt = k

                if not visited[nr][nc][0] or (visited[nr][nc][0] and visited[nr][nc][1] > cnt + cost):
                    visited[nr][nc] = (1, cnt + cost)
                    q.append((nr, nc, cost + cnt))

    return ans


ret = bfs(P)

print(ret) if ret != 0 else print(-1)
