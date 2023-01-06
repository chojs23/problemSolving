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
arr = list(input())
ans = 0
for idx in range(n):
    if arr[idx] == "P":
        for i in range(max(idx - k, 0), min(idx + k + 1, n)):
            if arr[i] == "H":
                arr[i] = 0
                ans += 1
                break
print(ans)
