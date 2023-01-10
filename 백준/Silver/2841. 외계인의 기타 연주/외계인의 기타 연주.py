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

N, P = map(int, input().split())

arr = list(list(map(int, input().split())) for _ in range(N))

clicked = [[] for _ in range(N + 1)]

res = 0
for a in arr:
    line, plat = a
    plat = -plat

    if clicked[line]:
        last = heapq.heappop(clicked[line])
    else:
        res += 1
        heapq.heappush(clicked[line], plat)
        continue

    if last > plat:
        heapq.heappush(clicked[line], plat)
        heapq.heappush(clicked[line], last)
        res += 1
    elif last < plat:
        if plat in clicked[line]:
            while heapq.heappop(clicked[line]) != plat:
                res += 1
            heapq.heappush(clicked[line], plat)
            res += 1
        else:
            res += 1
            heapq.heappush(clicked[line], plat)
            while heapq.heappop(clicked[line]) != plat:
                res += 1
            heapq.heappush(clicked[line], plat)
            res += 1
    else:
        heapq.heappush(clicked[line], last)
        continue


print(res)
