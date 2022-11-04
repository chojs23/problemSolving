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


N, M, G, R = map(int, input().split())

board = list(list(map(int, input().split())) for _ in range(N))


def bfs(sel, green):

    green_q = deque()
    red_q = deque()
    res = 0
    t_board = deepcopy(board)

    for row, col in sel:
        if (row, col) in green:
            green_q.append([row, col])  # 초록색 배양액
            t_board[row][col] = 3
        else:
            red_q.append([row, col])  # 빨간색 배양액
            t_board[row][col] = 4

    while green_q:
        green_temp = set()
        red_temp = set()
        while green_q:
            x, y = green_q.popleft()
            t_board[x][y] = 3
            for i in range(4):
                new_x, new_y = x + dr[i], y + dc[i]
                if 0 <= new_x < N and 0 <= new_y < M:
                    if t_board[new_x][new_y] == 1 or t_board[new_x][new_y] == 2:
                        green_temp.add((new_x, new_y))
        while red_q:
            x, y = red_q.popleft()
            t_board[x][y] = 4
            for i in range(4):
                new_x, new_y = x + dr[i], y + dc[i]
                if 0 <= new_x < N and 0 <= new_y < M:
                    if t_board[new_x][new_y] == 1 or t_board[new_x][new_y] == 2:
                        red_temp.add((new_x, new_y))

        inter = green_temp & red_temp
        green_temp = green_temp - inter
        red_temp = red_temp - inter
        for row, col in inter:
            t_board[row][col] = 5
            res += 1
        for row, col in green_temp:
            t_board[row][col] = 3
        for row, col in red_temp:
            t_board[row][col] = 4
        green_q.extend(green_temp)
        red_q.extend(red_temp)

    return res


possible = []

for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            possible.append((i, j))

answer = 0
# for c in combinations(possible, G + R):
#     green = c[:G]
#     red = c[G:]
#     answer = max(answer, bfs(green, red))


for selected in list(combinations(possible, G + R)):
    # selected를 green과 red로 나누기
    for green in list(combinations(selected, G)):

        answer = max(answer, bfs(selected, green))

print(answer)
