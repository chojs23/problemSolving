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


N = int(input())


level = []

head = []

for i in range(N):
    a = int(input())
    level.append(a)
    if a == 1:
        head.append(i)

if level[0] != 1:
    print(-1)
    exit()
ans = []

for i in range(1, N):
    if level[i - 1] + 1 < level[i]:
        print(-1)
        exit()

for i in range(N):
    size = 0
    for j in range(i + 1, N):
        if level[j] == level[i] + 1:
            size += 1
        if level[j] == level[i]:
            break
    ans.append(size)

for r in ans:
    print(r)
