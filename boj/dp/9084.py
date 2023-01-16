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
    val = list(map(int, input().split()))
    M = int(input())

    # 1, 5, 10, 50, 100, 500

    dp = [[0] * (M + 1) for _ in range(N + 1)]
    dp[0][0] = 1

    for i in range(1, N + 1):
        for j in range(M + 1):
            dp[i][j] += dp[i - 1][j]
            if j - val[i - 1] >= 0:
                dp[i][j] += dp[i][j - val[i - 1]]
    print(dp[N][M])
