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


n = int(input())
li = [int(input()) for _ in range(n)]

ip = True

if li[0] != 1:
    ip = False

if ip:
    for i in range(1, n):
        if li[i - 1] < li[i]:
            if li[i - 1] + 1 != li[i]:
                ip = False
                break

if not ip:
    print(-1)
else:
    result = [0] * n
    conts = [0] * 1000002
    for i in range(n - 1, -1, -1):
        v = li[i]

        result[i] = conts[v + 1]
        conts[v + 1] = 0

        conts[v] += 1

    for v in result:
        print(v)


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
