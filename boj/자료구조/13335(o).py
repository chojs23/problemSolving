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

# ==========================================================


n, w, l = map(int, input().split())

a = list(map(int, input().split()))
ans = 0
bridge = [0]*w
while True:
    if not a:
        break

    ans += 1

    if sum(bridge[1:])+a[0] <= l:
        bridge = bridge[1:]
        bridge.append(a.pop(0))
    else:
        bridge = bridge[1:]
        bridge.append(0)

    # print(bridge)

while True:
    if sum(bridge) != 0:
        bridge = bridge[1:]
        ans += 1
    else:
        break


print(ans)
