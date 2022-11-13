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

T = int(input())


def bfs(start, fire):
    q1 = deque()
    a, b = start
    for f in fire:
        q1.append(f)
    q2 = deque()
    q2.append([a, b])

    visited = [[0] * w for _ in range(h)]
    visited[a][b] = 1
    res = 0
    while q2:

        for _ in range(len(q1)):
            r, c = q1.popleft()
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < h and 0 <= nc < w:
                    if arr[nr][nc] == "." or arr[nr][nc] == "@":
                        arr[nr][nc] = "*"
                        q1.append([nr, nc])

        for _ in range(len(q2)):
            r, c = q2.popleft()

            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if not (0 <= nr < h) or not (0 <= nc < w):
                    return res + 1
                if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc]:
                    if arr[nr][nc] == ".":
                        visited[nr][nc] = 1
                        q2.append([nr, nc])
        res += 1

    return "IMPOSSIBLE"


for _ in range(T):
    w, h = map(int, input().split())

    arr = [list(input().rstrip()) for _ in range(h)]
    fire = []
    for i, r in enumerate(arr):
        for j, c in enumerate(r):
            if c == "@":
                start = [i, j]
            if c == "*":
                fire.append([i, j])

    print(bfs(start, fire))
