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

n = int(input())

arr = list(map(int, input().split()))

arr.sort()

res = INF

ans = []

for i in range(n - 2):
    cur = arr[i]
    l, r = i + 1, n - 1
    while l < r:
        cur_sum = cur + arr[l] + arr[r]
        if abs(cur_sum) <= abs(res):
            ans = [cur, arr[l], arr[r]]
            res = cur_sum
        if cur_sum < 0:
            l += 1
        elif cur_sum > 0:
            r -= 1
        else:
            print(*ans)
            sys.exit()

print(*ans)
