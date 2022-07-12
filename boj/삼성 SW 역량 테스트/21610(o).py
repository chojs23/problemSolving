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


dr, dc = [0, -1, -1, -1, 0, 1, 1, 1], [-1, -1, 0, 1, 1, 1, 0, -1]


n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
oper = [list(map(int, input().split())) for _ in range(m)]

cloud = [[n - 1, 0], [n - 1, 1], [n - 2, 0], [n - 2, 1]]
cloud2 = []

visited = [[0] * n for _ in range(n)]


def move(i):
    for cl in cloud:
        r, c = cl
        d, s = oper[i]
        nr, nc = r + dr[d - 1] * s, c + dc[d - 1] * s

        cloud2.append([(n + nr) % n, (n + nc) % n])
        visited[(n + nr) % n][(n + nc) % n] = 1


def watering():
    for cl in cloud2:
        r, c = cl
        arr[r][c] += 1


def bug():
    for cl in cloud2:
        r, c = cl
        cnt = 0
        for i in range(1, 8, 2):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] > 0:
                cnt += 1

        arr[r][c] += cnt


visited = [[0] * n for _ in range(n)]


def new_cloud():
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and arr[i][j] >= 2:
                cloud.append([i, j])
                arr[i][j] -= 2


for i in range(len(oper)):
    visited = [[0] * n for _ in range(n)]
    move(i)
    watering()
    bug()
    cloud.clear()
    new_cloud()
    cloud2.clear()

ans = 0

for a in arr:
    ans += sum(a)
print(ans)
