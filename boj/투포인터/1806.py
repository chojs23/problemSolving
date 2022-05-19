from copy import copy, deepcopy
import sys
from collections import defaultdict, deque
from itertools import permutations
import heapq

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

input = sys.stdin.readline

# ===========================================================

n, s = map(int, input().split())

arr = list(map(int, input().split()))


ans = 100001

l, r = 0, 0

sum = arr[0]
while l < n:

    if sum >= s:
        ans = min(ans, r - l + 1)
        sum -= arr[l]
        l += 1
    else:
        if r < n - 1:
            r += 1
            sum += arr[r]
        else:
            break

print(ans) if ans != 100001 else print(0)
