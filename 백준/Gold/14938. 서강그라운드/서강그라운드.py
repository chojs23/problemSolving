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

n, m, r = map(int, input().split())

item = list(map(int, input().split()))

graph = [[] for _ in range(n + 1)]

# [cur,next,cost]
for _ in range(r):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])


def dijkstra(start):
    distance = [INF] * (n + 1)
    distance[start] = 0
    q = []
    # [cost,node]
    heapq.heappush(q, [0, start])
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, [cost, i[0]])
    return distance


ans = 0
for time in range(1, n + 1):
    distance = dijkstra(time)
    res = 0
    for i in range(1, n + 1):
        if distance[i] <= m:
            res += item[i - 1]
    ans = max(ans, res)
print(ans)
