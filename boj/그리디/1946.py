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
for _ in range(T):
    N = int(input())
    res = 1
    arr = [list(map(int, input().split())) for _ in range(N)]

    arr = sorted(arr, key=lambda x: x[0])
    top = 0
    for i in range(1, N):
        if arr[i][1] < arr[top][1]:
            top = i
            res += 1

    print(res)
