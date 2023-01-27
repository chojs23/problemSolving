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

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


def bfs(start):
    q = deque()
    q.append(start)
    visited = [[0, 0] for _ in range(n + 1)]
    visited[start][0] = 1

    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i][0]:
                visited[i] = [1, visited[now][1] + 1]
                q.append(i)

    return visited


visited = bfs(x)
flag = 0
for i in range(n + 1):
    if visited[i][1] == k:
        print(i)
        flag = 1
if not flag:
    print(-1)
