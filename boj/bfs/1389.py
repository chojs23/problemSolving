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


N, M = map(int, input().split())
arr = [list() for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)


def bfs(start):
    q = deque()
    q.append((start, 0))
    res = 0
    visited = [False] * (N + 1)
    visited[start] = True
    while q:
        now, cnt = q.popleft()
        res += cnt
        for next in arr[now]:
            if not visited[next]:
                visited[next] = True
                q.append((next, cnt + 1))
    return res


minRes = INF

for i in range(1, N + 1):
    temp = bfs(i)
    if minRes > temp:
        minRes = temp
        res = i

print(res)
