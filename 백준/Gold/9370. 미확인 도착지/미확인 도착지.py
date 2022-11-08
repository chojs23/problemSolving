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


def dijkstra(start):
    heap = []
    heapq.heappush(heap, [0, start])
    dp = [100000000 for i in range(n + 1)]
    dp[start] = 0
    while heap:
        we, nu = heapq.heappop(heap)
        for ne, nw in s[nu]:
            wei = we + nw
            if dp[ne] > wei:
                dp[ne] = wei
                heapq.heappush(heap, [wei, ne])
    return dp

    
t = int(input())
for _ in range(t):
    n, m, c = map(int, input().split())
    start, g, h = map(int, input().split())
    s = [[] for i in range(n + 1)]
    de = []
    for j in range(m):
        a, b, d = map(int, input().split())
        s[a].append([b, d])
        s[b].append([a, d])
    for k in range(c):
        de.append(int(input()))
    start_ = dijkstra(start)
    g_ = dijkstra(g)
    h_ = dijkstra(h)
    an = []
    for l in de:
        if start_[g] + g_[h] + h_[l] == start_[l] or start_[h] + h_[g] + g_[l] == start_[l]:
            an.append(l)
    an.sort()
    for f in an:
        print(f, end=' ')
    print()