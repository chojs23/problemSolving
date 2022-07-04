from copy import copy, deepcopy
from math import sqrt
import sys
from collections import defaultdict, deque
from itertools import combinations, permutations
import heapq
import bisect

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

input = sys.stdin.readline
INF = sys.maxsize

# ===========================================================


def check(nx, ny):
    if len(chess[nx][ny]) >= 4:
        return True
    return False


def nw(x, y, nx, ny):
    first = chess[x][y].index(j)
    last = len(chess[x][y])
    for k in range(first, last):
        ch[chess[x][y][k]][0] = nx
        ch[chess[x][y][k]][1] = ny
        chess[nx][ny].append(chess[x][y][k])
    for _ in range(first, last):
        chess[x][y].pop()


def nr(x, y, nx, ny):
    first = chess[x][y].index(j)
    last = len(chess[x][y])
    for k in range(last - 1, first - 1, -1):
        ch[chess[x][y][k]][0] = nx
        ch[chess[x][y][k]][1] = ny
        chess[nx][ny].append(chess[x][y][k])
    for _ in range(first, last):
        chess[x][y].pop()


dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
n, k = map(int, input().split())
cb = []
ch = []
chess = [[deque() for i in range(n)] for i in range(n)]
for i in range(n):
    cb.append(list(map(int, input().split())))
for i in range(k):
    x, y, d = map(int, input().split())
    chess[x - 1][y - 1].append(i)
    ch.append([x - 1, y - 1, d])
for i in range(1, 1001):
    for j in range(k):
        x, y, d = ch[j]
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < n and cb[nx][ny] == 0:
            nw(x, y, nx, ny)
            if check(nx, ny):
                print(i)
                exit()
        elif 0 <= nx < n and 0 <= ny < n and cb[nx][ny] == 1:
            nr(x, y, nx, ny)
            if check(nx, ny):
                print(i)
                exit()
        elif not (0 <= nx < n and 0 <= ny < n) or cb[nx][ny] == 2:
            if d == 1:
                d = 2
            elif d == 2:
                d = 1
            elif d == 3:
                d = 4
            elif d == 4:
                d = 3
            ch[j][2] = d
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and cb[nx][ny] == 0:
                nw(x, y, nx, ny)
                if check(nx, ny):
                    print(i)
                    exit()
            elif 0 <= nx < n and 0 <= ny < n and cb[nx][ny] == 1:
                nr(x, y, nx, ny)
                if check(nx, ny):
                    print(i)
                    exit()
else:
    print(-1)
