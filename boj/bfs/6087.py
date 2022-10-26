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


w, h = map(int, input().split())

board = []
for _ in range(h):
    board.append(list(input().strip()))

visited = [[INF]*w for _ in range(h)]


def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dr[i], y + dc[i]
            while True:
                # 범위를 벗어난다
                if not (0 <= nx < h and 0 <= ny < w):
                    break
                # 벽을 만난다
                if board[nx][ny] == "*":
                    break
                # 지난 적 있는 곳인데, 지금 경로로는 너무 많은 거울이 필요해서 break
                if visited[nx][ny] < visited[x][y] + 1:
                    break
                # board업데이트, queue 추가
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                nx = nx + dr[i]
                ny = ny + dc[i]


s = []
for i in range(h):
    for j in range(w):
        if board[i][j] == "C":
            s.append([i, j])

bfs(s[0][0], s[0][1])
print(visited[s[1][0]][s[1][1]]-1)
