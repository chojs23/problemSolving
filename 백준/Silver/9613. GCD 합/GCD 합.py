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


t = int(input())


for _ in range(t):
    nums = list(map(int, input().split()))
    n = nums.pop(0)
    res = 0
    for c in combinations(nums, 2):
        a = math.gcd(c[0], c[1])
        res += a

    print(res)
