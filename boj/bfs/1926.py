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


n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]


def bfs(r, c):

    if visited[r][c]:
        return False
    q = deque()

    q.append([r, c])
    visited[r][c] = 1
    ret = 1

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 1 and not visited[nr][nc]:
                q.append([nr, nc])
                visited[nr][nc] = 1
                ret += 1

    return ret


ans = 0
res = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            ret = bfs(i, j)
            if ret:
                res = max(res, ret)
                ans += 1

print(ans)
print(res)
