from copy import copy, deepcopy
import sys
from collections import defaultdict, deque
from itertools import permutations
import heapq

dr, dc = [-1, 1, 0, 0], [0, 0, 1, -1]

input = sys.stdin.readline
INF = sys.maxsize

# ===========================================================

n, m = map(int, input().split())


parent = [i for i in range(n + 1)]
road = []
for i in range(m):
    start, end, cost = map(int, input().split())
    road.append([start, end, cost])

road = sorted(road, key=lambda x: x[2])


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


cnt = 0
res = 0
for r in road:
    if cnt == n - 2:
        break
    start, end, cost = r

    if find_parent(parent, start) == find_parent(parent, end):
        continue

    union_parent(parent, start, end)
    res += cost
    cnt += 1

print(res)
