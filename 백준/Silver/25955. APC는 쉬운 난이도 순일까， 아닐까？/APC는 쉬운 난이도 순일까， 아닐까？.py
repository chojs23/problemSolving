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


N = int(input())

tier = ["B", "S", "G", "P", "D"]

arr = list(input().split())
original = arr.copy()

# 1 3 4 5 7 9 10 17 13 11 15 20

for i, a in enumerate(arr):
    t = a[0]
    p = int(a[1:])
    arr[i] = tier.index(t) * 1000 + (1000 - p)

prev = arr[0]

temp1 = -1
for i in range(1, N):
    if arr[i] < prev:
        temp1 = i - 1
        break
    prev = arr[i]

temp2 = -1
prev = arr[N - 1]
for i in range(N - 1, -1, -1):
    if arr[i] > prev:
        temp2 = i + 1
        break
    prev = arr[i]

if temp1 != -1:
    print("KO")
    print(original[temp2], original[temp1])
else:
    print("OK")
