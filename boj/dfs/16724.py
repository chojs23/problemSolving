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


n, m = map(int, input().split())

arr = []

for i in range(n):
    arr.append(list(map(str, input().rstrip())))


parent = [i for i in range(n * m)]


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def dfs(r, c):
    if visited[r][c]:
        return
    visited[r][c] = 1
    num = r * m + c
    if arr[r][c] == "U":
        nr, nc = r + dr[0], c + dc[0]
    elif arr[r][c] == "D":
        nr, nc = r + dr[1], c + dc[1]
    elif arr[r][c] == "L":
        nr, nc = r + dr[2], c + dc[2]
    else:
        nr, nc = r + dr[3], c + dc[3]
    next_num = nr * m + nc
    if 0 <= nr < n and 0 <= nc < m and find_parent(num) != find_parent(next_num):
        union_parent(num, next_num)
        dfs(nr, nc)


ans = 0

visited = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            dfs(i, j)

# visited2 = dict()
# for i in range(n * m):
#     if find_parent(parent[i]) not in visited2:
#         ans += 1
#         visited2[parent[i]] = True
print(parent)
for i in range(n * m):
    find_parent(i)
print(parent)
print(len(set(parent)))
