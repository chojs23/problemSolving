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

ans = []

res = INF

l, r = 0, n - 1

while l < r:
    cur_sum = arr[l] + arr[r]

    if cur_sum == 0:
        print(arr[l], arr[r])
        sys.exit()

    if abs(cur_sum) <= abs(res):
        ans = [arr[l], arr[r]]
        res = ans[0] + ans[1]

    if cur_sum < 0:
        l += 1
    else:
        r -= 1

print(*ans)
