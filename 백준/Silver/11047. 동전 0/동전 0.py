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

n, k = map(int, input().split())

a = list(int(input()) for _ in range(n))
ans = 0
for i in range(n - 1, -1, -1):
    if a[i] > k:
        continue

    while k >= a[i]:
        k -= a[i]
        ans += 1

    if k == 0:
        break

print(ans)
