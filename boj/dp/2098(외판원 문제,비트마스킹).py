from copy import copy, deepcopy
from math import sqrt
import sys
from collections import defaultdict, deque
from itertools import permutations
import heapq

dr, dc = [-1, 1, 0, 0], [0, 0, 1, -1]

input = sys.stdin.readline
INF = sys.maxsize

# ===========================================================

N = int(input())
dp = [[INF] * (1 << N) for _ in range(N)]
w = list(list(map(int, input().split())) for _ in range(N))


def dfs(x, visited):
    if visited == (1 << N) - 1:
        if w[x][0]:
            return w[x][0]
        else:
            return INF

    if dp[x][visited] != INF:
        return dp[x][visited]

    for i in range(1, N):
        if not w[x][i]:
            continue
        if visited & (1 << i):
            continue

        dp[x][visited] = min(dp[x][visited], dfs(i, visited | (1 << i)) + w[x][i])

    return dp[x][visited]


print(dfs(0, 1))
