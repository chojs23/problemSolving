import collections
import itertools
from copy import copy, deepcopy
from math import sqrt
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

K = int(input())

size = 1
count = 0

while size < K:
    size = size << 1

size2 = size

while K > 0:
    if K >= size:
        K -= size
    else:
        size //= 2
        count += 1

print(size2, count)
