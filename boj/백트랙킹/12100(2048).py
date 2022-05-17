from copy import copy, deepcopy
import sys
from collections import defaultdict, deque
from itertools import permutations
import heapq

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

input = sys.stdin.readline

# ===========================================================

n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))


def move(board, dir):
    if dir == 0:  # 동쪽
        for i in range(n):
            top = n - 1
            for j in range(n - 2, -1, -1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][top] == 0:
                        board[i][top] = tmp
                    elif board[i][top] == tmp:
                        board[i][top] = tmp * 2
                        top -= 1
                    else:
                        top -= 1
                        board[i][top] = tmp

    elif dir == 1:  # 서쪽
        for i in range(n):
            top = 0
            for j in range(1, n):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][top] == 0:
                        board[i][top] = tmp
                    elif board[i][top] == tmp:
                        board[i][top] = tmp * 2
                        top += 1
                    else:
                        top += 1
                        board[i][top] = tmp

    elif dir == 2:  # 남쪽
        for j in range(n):
            top = n - 1
            for i in range(n - 2, -1, -1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[top][j] == 0:
                        board[top][j] = tmp
                    elif board[top][j] == tmp:
                        board[top][j] = tmp * 2
                        top -= 1
                    else:
                        top -= 1
                        board[top][j] = tmp

    else:
        for j in range(n):
            top = 0
            for i in range(1, n):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[top][j] == 0:
                        board[top][j] = tmp
                    elif board[top][j] == tmp:
                        board[top][j] = tmp * 2
                        top += 1
                    else:
                        top += 1
                        board[top][j] = tmp

    return board


def dfs(board, cnt):
    global res
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                res = max(res, board[i][j])
        return

    for i in range(4):
        tmp_board = move(deepcopy(board), i)
        dfs(tmp_board, cnt + 1)


res = 0
dfs(graph, 0)
print(res)
