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

a, b, c = map(int, input().split())
visited = [[False] * 1501 for _ in range(1501)]
tot = a + b + c


def bfs():
    global a, b, c
    q = deque()
    q.append([a, b])
    visited[a][b] = True
    while q:
        a, b = q.popleft()
        c = tot - a - b
        if a == b == c:
            return 1
        for na, nb in ((a, b), (a, c), (b, c)):
            if na < nb:
                nb -= na
                na += na
            elif na > nb:
                na -= nb
                nb += nb
            else:
                continue
            nc = tot - na - nb
            # a = min(na, nb, nc)
            # b = max(na, nb, nc)
            if not visited[na][nb]:
                q.append((na, nb))
                visited[na][nb] = True
    return 0


if tot % 3 != 0:
    print(0)
else:
    print(bfs())
