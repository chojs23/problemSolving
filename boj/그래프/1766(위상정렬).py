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

n, m = map(int, input().rstrip().split())

graph = [[] for _ in range(n + 1)]
inDegree = [0 for _ in range(n + 1)]
q = []

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    inDegree[b] += 1

for i in range(1, n + 1):
    if inDegree[i] == 0:
        heapq.heappush(q, i)

ans = []
while q:
    tmp = heapq.heappop(q)
    ans.append(tmp)
    for i in graph[tmp]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            heapq.heappush(q, i)

print(" ".join(map(str, ans)))
