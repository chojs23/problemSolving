from copy import copy, deepcopy
from math import sqrt
import sys
from collections import defaultdict, deque
from itertools import permutations
import heapq

dr, dc = [-1, 1, 0, 0], [0, 0, 1, -1]

input = sys.stdin.readline
INF = sys.maxsize

# ===========================================================

n = int(input())

parent = [i for i in range(n)]


def get_distance(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


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


coordinate = []

for i in range(n):
    coordinate.append(list(map(float, input().split())))

road = []

for i in range(n):
    for j in range(i + 1, n):
        x1, y1 = coordinate[i]
        x2, y2 = coordinate[j]
        road.append([i, j, get_distance(x1, y1, x2, y2)])

road = sorted(road, key=lambda x: x[2])

ans = 0

for r in road:
    start, end, cost = r
    sp = find_parent(parent, start)
    ep = find_parent(parent, end)

    if sp != ep:

        union_parent(parent, start, end)
        ans += cost


print(round(ans, 2))
