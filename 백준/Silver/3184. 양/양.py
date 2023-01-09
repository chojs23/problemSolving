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

R, C = map(int, input().split())

# . empty # wall o sheep v wolf

board = [list(input().rstrip()) for _ in range(R)]


visited = [[0] * C for _ in range(R)]


def bfs(startR, startC):
    q = deque()
    q.append((startR, startC))
    sheep, wolf = 0, 0
    while q:

        r, c = q.popleft()
        if board[r][c] == "o":
            sheep += 1
        elif board[r][c] == "v":
            wolf += 1
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and board[nr][nc] != "#":
                visited[nr][nc] = 1
                q.append((nr, nc))
    if sheep > wolf:
        wolf = 0
    else:
        sheep = 0
    return sheep, wolf


sheep, wolf = 0, 0
for i in range(R):
    for j in range(C):
        if visited[i][j] == 0 and board[i][j] != "#":
            visited[i][j] = 1
            s, w = bfs(i, j)
            sheep += s
            wolf += w

print(sheep, wolf)
