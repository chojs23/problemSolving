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

n, m, k = map(int, input().split())

a = []
tree = [[[] for _ in range(n)] for _ in range(n)]
# tree2 = [[deque() for _ in range(n)] for _ in range(n)]

board = [[5] * n for _ in range(n)]

for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(m):
    x, y, z = map(int, input().split())
    tree[x - 1][y - 1].append(z)

# print(tree)

for i in range(n):
    for j in range(n):
        tree[i][j].sort()
        tree[i][j] = deque(tree[i][j])


def spring(tree):
    # print("spring come")
    # tree = sorted(tree, key=lambda x: x[2])
    # print(tree)
    for i in range(n):
        for j in range(n):
            temp = deque()
            next_board = 0
            for k in range(len(tree[i][j])):
                z = tree[i][j][k]
                if board[i][j] >= z:
                    board[i][j] -= z
                    temp.append(z + 1)
                else:
                    next_board += z // 2
            tree[i][j] = temp
            board[i][j] += next_board

    return tree


dx, dy = [1, -1, 0, 0, 1, 1, -1, -1], [0, 0, 1, -1, 1, -1, 1, -1]


def fall(tree):
    add = []
    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                for k in tree[i][j]:
                    if k % 5 == 0:
                        for d in range(8):
                            nx, ny = i + dx[d], j + dy[d]
                            if 0 <= nx < n and 0 <= ny < n:
                                add.append([nx, ny, 1])

    for a in add:
        tree[a[0]][a[1]].appendleft(1)

    return tree


def winter():
    for i in range(n):
        for j in range(n):
            board[i][j] += a[i][j]


for u in range(k):
    # print(u)
    # print(board)
    tree = spring(tree)
    # print("tree", tree)
    # print("dead", dead)
    # print(board)

    # summer(tree, dead)

    # print("fall come")
    tree = fall(tree)
    # print("winter come")

    winter()

# print(tree)
ans = 0
for i in range(n):
    for j in range(n):
        if tree[i][j]:
            ans += len(tree[i][j])
print(ans)
