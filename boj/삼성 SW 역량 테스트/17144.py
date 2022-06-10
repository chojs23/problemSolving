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


def diff():
    temp = [[0] * c for i in range(r)]
    temp[t1][t2] = -1
    temp[b1][b2] = -1
    for i in range(r):
        for j in range(c):
            if s[i][j] > 0:
                cnt = 0
                for k in range(4):
                    x = i + dx[k]
                    y = j + dy[k]
                    if 0 <= x < r and 0 <= y < c and s[x][y] != -1:
                        temp[x][y] += s[i][j] // 5
                        cnt += 1
                temp[i][j] += s[i][j] - (s[i][j] // 5 * cnt)
    return temp


def clar(x, y, dir):
    temp = deepcopy(s)
    cx, cy = x, y - 1
    s[x][y] = 0
    for i in range(4):
        while True:
            nx = x + dx[dir[i]]
            ny = y + dy[dir[i]]
            if nx == cx and ny == cy:
                return
            if 0 <= nx < r and 0 <= ny < c:
                s[nx][ny] = temp[x][y]
            else:
                break
            x, y = nx, ny


dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

r, c, t = map(int, input().split())
s = []
cl = []

for i in range(r):
    a = list(map(int, input().split()))
    s.append(a)
    for j in range(c):
        if a[j] == -1:
            cl.append([i, j])

t1, t2 = cl[0][0], cl[0][1]
b1, b2 = cl[1][0], cl[1][1]

for i in range(t):
    s = diff()
    clar(t1, t2 + 1, [3, 1, 2, 0])
    clar(b1, b2 + 1, [3, 0, 2, 1])
s[t1][t2], s[b1][b2] = 0, 0
result = 0
for i in range(r):
    result += sum(s[i])
print(result)
