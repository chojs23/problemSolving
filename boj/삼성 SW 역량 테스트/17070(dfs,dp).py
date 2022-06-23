from copy import copy, deepcopy
from math import sqrt
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

s = [list(map(int, input().split())) for _ in range(n)]

count = 0


def dfs(x, y, direction):
    global count
    if x == n - 1 and y == n - 1:
        count += 1
    if direction == 0:
        if y + 1 < n and s[x][y + 1] == 0:
            dfs(x, y + 1, 0)
        if x + 1 < n and y + 1 < n:
            if s[x][y + 1] == 0 and s[x + 1][y + 1] == 0 and s[x + 1][y] == 0:
                dfs(x + 1, y + 1, 2)
    elif direction == 1:
        if x + 1 < n and s[x + 1][y] == 0:
            dfs(x + 1, y, 1)
        if x + 1 < n and y + 1 < n:
            if s[x][y + 1] == 0 and s[x + 1][y + 1] == 0 and s[x + 1][y] == 0:
                dfs(x + 1, y + 1, 2)
    elif direction == 2:
        if y + 1 < n and s[x][y + 1] == 0:
            dfs(x, y + 1, 0)
        if x + 1 < n and s[x + 1][y] == 0:
            dfs(x + 1, y, 1)
        if x + 1 < n and y + 1 < n:
            if s[x][y + 1] == 0 and s[x + 1][y + 1] == 0 and s[x + 1][y] == 0:
                dfs(x + 1, y + 1, 2)


dfs(0, 1, 0)
print(count)

# =================================================
# dp

import sys

input = sys.stdin.readline
n = int(input())
s = [list(map(int, input().split())) for i in range(n)]
result = [[[0 for i in range(n)] for i in range(n)] for i in range(3)]
result[0][0][1] = 1
for i in range(2, n):
    if s[0][i] == 0:
        result[0][0][i] = result[0][0][i - 1]
for i in range(1, n):
    for j in range(2, n):
        if s[i][j] == 0 and s[i - 1][j] == 0 and s[i][j - 1] == 0:
            result[2][i][j] = (
                result[0][i - 1][j - 1]
                + result[1][i - 1][j - 1]
                + result[2][i - 1][j - 1]
            )
        if s[i][j] == 0:
            result[0][i][j] = result[0][i][j - 1] + result[2][i][j - 1]
            result[1][i][j] = result[1][i - 1][j] + result[2][i - 1][j]
print(result[0][n - 1][n - 1] + result[1][n - 1][n - 1] + result[2][n - 1][n - 1])
