from copy import copy, deepcopy
import sys
from collections import defaultdict, deque
from itertools import permutations
import heapq

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

input = sys.stdin.readline

# ===========================================================

n, k = map(int, input().split())

jew = []
bag = []
for i in range(n):
    m, v = map(int, input().split())
    jew.append([m, v])

jew.sort()

for i in range(k):
    bag.append(int(input()))
bag.sort()


idx = 0
res = 0
q = []


for b in bag:
    while idx < n and b >= jew[idx][0]:
        heapq.heappush(q, -jew[idx][1])
        idx += 1

    if q:
        res += -heapq.heappop(q)


print(res)
