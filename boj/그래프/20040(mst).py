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


n, m = map(int, input().split())

parent = [i for i in range(n)]


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


for i in range(m):
    a, b = map(int, input().split())

    ap = find_parent(a)
    bp = find_parent(b)

    if ap == bp:
        print(i + 1)
        sys.exit()

    union_parent(a, b)

print(0)
