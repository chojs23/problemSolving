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


n1, n2 = map(int, input().split())

a = list(map(str, input().rstrip()))
b = list(map(str, input().rstrip()))
a.reverse()
t = int(input())


c = a + b

for _ in range(t):
    for i in range(len(c) - 1):
        if c[i] in a and c[i + 1] in b:
            c[i], c[i + 1] = c[i + 1], c[i]

            if c[i + 1] == a[-1]:
                break

print("".join(c))
