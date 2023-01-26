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

board = list(list(input().rstrip()) for _ in range(5))
p = []
res = set()


def backtrack(arr, index=0, S=0, Y=0):
    tmp = arr
    if Y > 3:
        return
    if index == 6:
        arr.sort()
        res.add(tuple(arr))
    else:
        adjacents = []
        for node in range(len(arr)):
            for i in range(4):
                dx = arr[node][0] + dr[i]
                dy = arr[node][1] + dc[i]
                if 0 > dx or 5 <= dx or 0 > dy or 5 <= dy:
                    continue
                if (dx, dy) in arr:
                    continue
                adjacents.append((dx, dy))
        for adjacent in adjacents:
            nx = adjacent[0]
            ny = adjacent[1]
            if board[nx][ny] == "S":
                backtrack(arr + [(nx, ny)], index + 1, S + 1, Y)
            else:
                backtrack(arr + [(nx, ny)], index + 1, S, Y + 1)


for i in range(5):
    for j in range(5):
        if board[i][j] == "S":
            backtrack([(i, j)], index=0, S=1)

print(len(res))
