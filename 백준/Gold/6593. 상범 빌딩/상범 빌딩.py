import collections
import itertools
from copy import copy, deepcopy
from math import sqrt
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

df = [1, -1]


def bfs(building, start, end):
    q = deque()
    f, r, c = start
    ef, er, ec = end
    time = 0
    q.append([f, r, c, time])
    visited = [list([0] * C for _ in range(R)) for _ in range(L)]
    visited[f][r][c] = 1
    while q:
        f, r, c, t = q.popleft()
        if [f, r, c] == [ef, er, ec]:
            return t

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < R and 0 <= nc < C and not visited[f][nr][nc]:
                if building[f][nr][nc] == "." or building[f][nr][nc] == "E":
                    q.append([f, nr, nc, t + 1])
                    visited[f][nr][nc] = 1

        for i in range(2):
            nf = f + df[i]
            if 0 <= nf < L and not visited[nf][r][c]:
                if building[nf][r][c] == "." or building[nf][r][c] == "E":
                    q.append([nf, r, c, t + 1])
                    visited[nf][r][c] = 1

    return 0


while True:
    L, R, C = map(int, input().split())

    if L == R == C == 0:
        break

    building = []

    for l in range(L):
        arr = [list(input().rstrip()) for _ in range(R)]

        for i in range(R):
            for j in range(C):
                if arr[i][j] == "S":
                    start = [l, i, j]
                if arr[i][j] == "E":
                    end = [l, i, j]

        building.append(arr)
        input()

    ans = 0

    ans = bfs(building, start, end)

    print("Escaped in {} minute(s).".format(ans)) if ans != 0 else print("Trapped!")
