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

# ===========================================================

N = int(input())

q = deque(range(1, N+1))

while True:
    if len(q) == 1:
        break
    q.popleft()
    if len(q) == 1:
        break
    a = q.popleft()
    q.append(a)

print(q[0])
