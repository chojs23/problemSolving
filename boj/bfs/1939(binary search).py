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
graph = [list() for _ in range(N + 1)]

for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

start, end = map(int, input().split())


def bfs(mid):
    visited[start] = 1
    q = deque()
    q.append(start)

    while q:
        now = q.popleft()
        if now == end:
            return True

        for nxt, weight in graph[now]:
            if not visited[nxt] and weight >= mid:
                q.append(nxt)
                visited[nxt] = 1

    return False


left, right = 1, 1000000000

while left <= right:
    visited = [0] * (N + 1)
    mid = (left + right) // 2

    if bfs(mid):
        left = mid + 1
    else:
        right = mid - 1


print(right)
