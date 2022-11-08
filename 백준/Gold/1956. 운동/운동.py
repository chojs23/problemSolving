import collections
import itertools
from copy import copy, deepcopy
from math import sqrt
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

v, e = map(int, sys.stdin.readline().split())
inf = 100000000
s = [[inf] * v for i in range(v)]

for i in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    s[a - 1][b - 1] = c
for k in range(v):
    for i in range(v):
        for j in range(v):
            if s[i][j] > s[i][k] + s[k][j]:
                s[i][j] = s[i][k] + s[k][j]
result = inf
for i in range(v):
    result = min(result, s[i][i])
if result == inf:
    print(-1)
else:
    print(result)
