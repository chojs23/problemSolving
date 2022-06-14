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


n = int(input())
board = []

for i in range(n):
    board.append([0] * n)
k = int(input())

for i in range(k):
    a, b = map(int, input().split())
    board[a - 1][b - 1] = 1

l = int(input())

oper = []

for i in range(l):
    oper.append(list(input().split()))

cnt = 0
# 0 1 2 3 남 북 서 동
cur_dir = 3

board[0][0] = 2
head = (0, 0)
tail = (0, 0)

q = deque()


def move(cur_dir):
    global head
    global tail
    r, c = head
    q.append((r, c))
    if cur_dir == 0:

        nr, nc = r + 1, c
        if 0 <= nr < n and 0 <= nc < n:
            if board[nr][nc] == 0:
                head = (nr, nc)
                board[nr][nc] = 2
                if q:
                    tr, tc = q.popleft()
                    board[tr][tc] = 0
            elif board[nr][nc] == 1:
                board[nr][nc] = 2
                head = (nr, nc)

            else:
                return False
        else:
            return False
    if cur_dir == 1:
        nr, nc = r - 1, c
        if 0 <= nr < n and 0 <= nc < n:
            if board[nr][nc] == 0:
                head = (nr, nc)
                board[nr][nc] = 2
                if q:
                    tr, tc = q.popleft()
                    board[tr][tc] = 0

            elif board[nr][nc] == 1:
                board[nr][nc] = 2
                head = (nr, nc)
            else:
                return False
        else:
            return False
    if cur_dir == 2:
        nr, nc = r, c - 1
        if 0 <= nr < n and 0 <= nc < n:
            if board[nr][nc] == 0:
                head = (nr, nc)
                board[nr][nc] = 2
                if q:
                    tr, tc = q.popleft()
                    board[tr][tc] = 0

            elif board[nr][nc] == 1:
                board[nr][nc] = 2
                head = (nr, nc)
            else:
                return False
        else:
            return False

    if cur_dir == 3:
        nr, nc = r, c + 1
        if 0 <= nr < n and 0 <= nc < n:
            if board[nr][nc] == 0:
                head = (nr, nc)
                board[nr][nc] = 2
                if q:
                    tr, tc = q.popleft()
                    board[tr][tc] = 0

            elif board[nr][nc] == 1:
                board[nr][nc] = 2
                head = (nr, nc)
            else:
                return False
        else:
            return False


idx = 0
while True:
    cnt += 1
    # print("cnt=", cnt)

    if move(cur_dir) == False:
        break

    if idx < len(oper) and cnt == int(oper[idx][0]):
        if oper[idx][1] == "L":
            if cur_dir == 0:
                cur_dir = 3
            elif cur_dir == 1:
                cur_dir = 2
            elif cur_dir == 2:
                cur_dir = 0
            else:
                cur_dir = 1
        else:
            if cur_dir == 0:
                cur_dir = 2
            elif cur_dir == 1:
                cur_dir = 3
            elif cur_dir == 2:
                cur_dir = 1
            else:
                cur_dir = 0
        idx += 1

print(cnt)
