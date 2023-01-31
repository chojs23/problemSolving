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

T = int(input())
n = int(input())

a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
aSum = []
for i in range(n):
    s = a[i]
    aSum.append(s)
    for j in range(i + 1, n):
        s += a[j]
        aSum.append(s)

bSum = []
for i in range(m):
    s = b[i]
    bSum.append(s)
    for j in range(i + 1, m):
        s += b[j]
        bSum.append(s)

aSum.sort()
bSum.sort()

ans = 0

for i in range(len(aSum)):
    ans += bisect.bisect_right(bSum, T - aSum[i]) - bisect.bisect_left(bSum, T - aSum[i])

print(ans)
