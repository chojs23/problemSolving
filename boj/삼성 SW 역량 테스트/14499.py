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


n, m, x, y, k = map(int, input().split())


board = []

for i in range(n):
    board.append(list(map(int, input().rstrip().split())))

oper = list(map(int, input().split()))

dice = [0, 0, 0, 0, 0, 0, 0]


def move(direction):
    if direction == 1:
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
    elif direction == 2:
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    elif direction == 3:
        dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]
    elif direction == 4:
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]


def dire(direction):
    if direction == 1:
        return 0, 1
    elif direction == 2:
        return 0, -1
    elif direction == 3:
        return -1, 0
    elif direction == 4:
        return 1, 0


for i in oper:
    a, b = dire(i)

    if 0 <= x + a < n and 0 <= y + b < m:
        x += a
        y += b
        move(i)
        if board[x][y] != 0:
            dice[1] = board[x][y]
            board[x][y] = 0
        else:
            board[x][y] = dice[1]
        print(dice[6])
