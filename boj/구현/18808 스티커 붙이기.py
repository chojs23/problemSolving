import collections
import itertools
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

# ==========================================================

# 스티커 90도 회전


def rotate_90(sticker_board):
    # r, c = len(sticker_board), len(sticker_board[0])
    # rotated_sticker_board = [[0] * r for _ in range(c)]
    # for i in range(c):
    #     for j in range(r):
    #         rotated_sticker_board[i][j] = sticker_board[r-j-1][i]
    rotated_sticker_board = list(zip(*sticker_board[::-1]))

    return rotated_sticker_board


def checking(temp, sticker):
    for sy in range(len(sticker)):
        for sx in range(len(sticker[0])):
            if temp[i+sy][j+sx] + sticker[sy][sx] > 1:
                return False
    return True


def attach(temp, sticker):
    for sy in range(len(sticker)):
        for sx in range(len(sticker[0])):
            temp[i+sy][j+sx] += sticker[sy][sx]
    return


Y, X, k = map(int, input().split())
notebook = [[0] * X for _ in range(Y)]

for _ in range(k):
    y, x = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(y)]
    chk = False
    cnt = 0
    while cnt < 4:
        if chk == True:
            break
        for i in range(Y - len(sticker) + 1):
            if chk == True:
                break
            for j in range(X - len(sticker[0]) + 1):
                if checking(notebook, sticker):
                    attach(notebook, sticker)
                    chk = True
                    break
        sticker = rotate_90(sticker)
        cnt += 1

answer = 0
for i in range(Y):
    for j in range(X):
        answer += notebook[i][j]

print(answer)
