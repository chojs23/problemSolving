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

n, m, k = map(int, input().split())
dp = [[1] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

if dp[n][m] < k:
    print(-1)
    exit(0)

res = ""
while True:
    if n == 0:
        res += "z" * m
        break
    if m == 0:
        res += "a" * n
        break

    if dp[n - 1][m] >= k:
        res += "a"
        n -= 1
    else:
        res += "z"
        k -= dp[n - 1][m]
        m -= 1

print(res)
