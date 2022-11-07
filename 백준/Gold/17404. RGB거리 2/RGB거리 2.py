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

N = int(input())

house = [list(map(int, input().split())) for _ in range(N)]

ans = INF

for i in range(3):
    dp = [[INF, INF, INF] for _ in range(N)]
    dp[0][i] = house[0][i]

    for j in range(1, N):
        dp[j][0] = house[j][0] + min(dp[j - 1][1], dp[j - 1][2])
        dp[j][1] = house[j][1] + min(dp[j - 1][0], dp[j - 1][2])
        dp[j][2] = house[j][2] + min(dp[j - 1][0], dp[j - 1][1])

    for j in range(3):
        if i != j:
            ans = min(ans, dp[-1][j])


print(ans)
