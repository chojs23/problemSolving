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

T = int(input())
for _ in range(T):
    N = int(input())
    X = list(map(int, input().split()))

    dp = [0] * (N)
    dp[0] = X[0]

    for i in range(1, N):
        dp[i] = max(dp[i - 1] + X[i], X[i])

    print(max(dp))
