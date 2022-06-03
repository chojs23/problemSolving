from copy import copy, deepcopy
from math import sqrt
import sys
from collections import defaultdict, deque
from itertools import permutations
import heapq

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

input = sys.stdin.readline
INF = sys.maxsize

# ===========================================================


board = []
for i in range(9):
    board.append(list(map(int, input().rstrip())))


def findUnassigned():
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return -1, -1


def print_board():
    for i in range(9):
        for j in range(9):
            print(board[i][j], end="")
        print()


def solve():
    row, col = findUnassigned()
    # no unassigned position is found, puzzle solved
    if row == -1 and col == -1:
        return True
    for num in range(1, 10):
        if isSafe(row, col, num):
            board[row][col] = num
            if solve():
                return True
            board[row][col] = 0
    return False


def isSafe(row, col, ch):
    boxrow = row - row % 3
    boxcol = col - col % 3
    if checkrow(row, ch) and checkcol(col, ch) and checksquare(boxrow, boxcol, ch):
        return True
    return False


def checkrow(row, ch):
    for col in range(9):
        if board[row][col] == ch:
            return False
    return True


def checkcol(col, ch):
    for row in range(9):
        if board[row][col] == ch:
            return False
    return True


def checksquare(row, col, ch):
    for r in range(row, row + 3):
        for c in range(col, col + 3):
            if board[r][c] == ch:
                return False
    return True


solve()
print_board()
