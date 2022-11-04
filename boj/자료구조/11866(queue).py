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


n, k = map(int, input().split())

q = deque()

for i in range(1, n + 1):
    q.append(i)


ans = []
while q:

    for _ in range(k - 1):
        cur = q.popleft()
        q.append(cur)
    cur = q.popleft()
    ans.append(cur)

print("<", end="")
print(*ans, sep=", ", end="")
print(">")
