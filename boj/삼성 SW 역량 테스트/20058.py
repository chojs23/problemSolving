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


n, q = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(2**n)]

l = list(map(int, input().split()))


def rotate(l):

    k = 2**l
    for x in range(0, 2**n, k):
        for y in range(0, 2**n, k):
            tmp = [board[i][y : y + k] for i in range(x, x + k)]
            for i in range(k):
                for j in range(k):
                    board[x + j][y + k - 1 - i] = tmp[i][j]


def check():
    cnt = [[0] * (2**n) for _ in range(2**n)]
    for r in range(2**n):
        for c in range(2**n):

            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]

                if 0 <= nr < 2**n and 0 <= nc < 2 ** n and board[nr][nc] > 0:
                    cnt[r][c] += 1

    for r in range(2**n):
        for c in range(2**n):
            if cnt[r][c] < 3 and board[r][c] > 0:
                board[r][c] -= 1


ans_pile = 0


def bfs(i, j):
    global ans_pile

    if visited[i][j] or board[i][j] == 0:
        return

    queue = deque()
    queue.append([i, j])
    cnt = 0

    while queue:
        cnt += 1
        r, c = queue.popleft()
        visited[r][c] = 1
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if (
                0 <= nr < 2**n
                and 0 <= nc < 2**n
                and not visited[nr][nc]
                and board[nr][nc]
            ):
                visited[nr][nc] = 1
                queue.append([nr, nc])

    ans_pile = max(ans_pile, cnt)


for i in l:
    rotate(i)

    check()

ans_sum = 0
for r in board:
    ans_sum += sum(r)

print(ans_sum)

visited = [[0] * (2**n) for _ in range(2**n)]
for i in range(2**n):
    for j in range(2**n):
        if board[i][j] > 0:
            bfs(i, j)

print(ans_pile)
