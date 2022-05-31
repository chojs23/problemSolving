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

planet = []

for i in range(n):
    x, y, z = map(int, sys.stdin.readline().split())
    planet.append([x, y, z, i])  # x,y,z좌표 i번째노드


e = []
for i in range(3):
    planet.sort(key=lambda x: x[i])  # 각 좌표별로 정렬
    start = planet[0][3]
    for j in range(1, n):  # 각 좌표별로 간선추가
        end = planet[j][3]
        e.append((start, end, abs(planet[j - 1][i] - planet[j][i])))
        start = end


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


e = sorted(e, key=lambda x: x[2])
parent = [i for i in range(n + 1)]

ans = 0
for r in e:
    start, end, cost = r

    sp = find_parent(parent, start)
    ep = find_parent(parent, end)

    if sp != ep:
        union_parent(parent, start, end)
        ans += cost

print(ans)
