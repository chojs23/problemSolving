import collections
import itertools
from copy import copy, deepcopy
from math import sqrt
import sys
from collections import defaultdict, deque
from itertools import combinations, permutations
import heapq
import bisect

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

input = sys.stdin.readline
INF = sys.maxsize

# ===========================================================


def bfs(same):
    start = same[0]
    q = collections.deque([start])
    visited = set([start])
    _sum = 0
    while q:
        v = q.popleft()
        _sum += pp[v]
        for u in g[v]:
            if u not in visited and u in same:
                q.append(u)
                visited.add(u)
    return _sum, len(visited)


n = int(sys.stdin.readline().strip())
pp = [int(x) for x in sys.stdin.readline().split()]
g = collections.defaultdict(list)
result = float('inf')

for i in range(n):
    _input = [int(x) for x in sys.stdin.readline().split()]
    for j in range(1, _input[0]+1):
        g[i].append(_input[j]-1)

for i in range(1, n//2 + 1):
    combis = list(combinations(range(n), i))
    for combi in combis:
        sum1, v1 = bfs(combi)
        sum2, v2 = bfs([i for i in range(n) if i not in combi])
        if v1 + v2 == n:  # 2번의 bfs를 통해 모든 노드가 방문되었는지 확인한다.
            result = min(result, abs(sum1 - sum2))

if result != float('inf'):
    print(result)
else:
    print(-1)
