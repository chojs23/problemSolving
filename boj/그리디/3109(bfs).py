import collections
import itertools
from copy import copy, deepcopy
from math import sqrt
import sys
from collections import defaultdict, deque
from itertools import combinations, permutations
import heapq
import bisect

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

input = sys.stdin.readline
INF = sys.maxsize

# ===========================================================


def solve(i, j):
    if j == c-1:
        return True

    for d in dx:
        if 0 <= i+d < r and table[i+d][j+1] == '.' and not visit[i+d][j+1]:
            visit[i+d][j+1] = True
            if solve(i+d, j+1):
                return True
    return False


r, c = map(int, input().split())
table = [list(input().rstrip()) for _ in range(r)]
visit = [[False] * c for _ in range(r)]
dx = [-1, 0, 1]
ans = 0
for i in range(r):
    if table[i][0] == '.':
        if solve(i, 0):
            ans += 1
print(ans)
