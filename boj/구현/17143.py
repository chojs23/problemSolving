from copy import copy, deepcopy
import sys
from collections import defaultdict, deque
from itertools import permutations
import heapq
from unittest import result

dr, dc = [-1, 1, 0, 0], [0, 0, 1, -1]

input = sys.stdin.readline
INF = sys.maxsize
# ===========================================================

R, C, M = map(int, input().split())


g = [[0] * C for i in range(R)]

for i in range(1, M + 1):
    r, c, s, d, z = map(int, input().split())
    g[r - 1][c - 1] = [s, d - 1, z]


def shMove():
    temp = [[0] * C for i in range(R)]
    for i in range(R):
        for j in range(C):
            if g[i][j] != 0:
                r, c, s, d, z = i, j, g[i][j][0], g[i][j][1], g[i][j][2]
                while s > 0:
                    r += dr[d]
                    c += dc[d]
                    if 0 <= r < R and 0 <= c < C:
                        s -= 1
                    else:
                        r -= dr[d]
                        c -= dc[d]
                        if d == 0:
                            d = 1
                        elif d == 1:
                            d = 0
                        elif d == 2:
                            d = 3
                        elif d == 3:
                            d = 2
                if temp[r][c] == 0:
                    temp[r][c] = [g[i][j][0], d, z]
                else:
                    if temp[r][c][2] < z:
                        temp[r][c] = [g[i][j][0], d, z]
    return temp


result = 0

for i in range(C):
    for j in range(R):
        if g[j][i] != 0:
            result += g[j][i][2]
            g[j][i] = 0
            break
    g = shMove()
print(result)
