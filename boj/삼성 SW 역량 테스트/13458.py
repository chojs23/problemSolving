from copy import copy, deepcopy
from math import sqrt
import sys
from collections import defaultdict, deque
from itertools import permutations
import heapq
import bisect

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

input = sys.stdin.readline
INF = sys.maxsize

# ===========================================================


n = int(input())


a = list(map(int, input().split()))

b, c = map(int, input().rstrip().split())

ans = 0

for i in range(n):
    a[i] -= b
    ans += 1

    if a[i] > 0:
        div, mod = divmod(a[i], c)
        if mod > 0:
            ans += div + 1
        else:
            ans += div

print(ans)
