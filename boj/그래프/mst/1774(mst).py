import collections
import itertools
from copy import copy, deepcopy
import math
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

N, M = map(int, input().split())

parent = [i for i in range(N + 1)]


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


points = [[]]
# calculate distance between two points
def calculate(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


for _ in range(N):
    x, y = map(int, input().split())
    points.append([x, y])

for _ in range(M):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

possible = []

for i in range(1, N):
    for j in range(i + 1, N + 1):
        possible.append([i, j, calculate(points[i], points[j])])

ans = 0

possible.sort(key=lambda x: x[2])

for p in possible:
    x, y, cost = p

    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        ans += cost

print("%.2f" % ans)
