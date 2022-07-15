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

N, M, K = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

oper = [list(map(int, input().split())) for _ in range(K)]


ans = INF

for o in permutations(oper, K):
    arr_copy = deepcopy(arr)
    for r, c, s, in o:

        r -= 1
        c -= 1

        for n in range(s, 0, -1):
            temp = arr_copy[r-n][c+n]
            arr_copy[r-n][c-n+1:c+n+1] = arr_copy[r-n][c-n:c+n]  # right
            for row in range(r-n, r+n):  # up
                arr_copy[row][c-n] = arr_copy[row+1][c-n]
            arr_copy[r+n][c-n:c+n] = arr_copy[r+n][c-n+1:c+n+1]  # left
            for row in range(r+n, r-n, -1):  # down
                arr_copy[row][c+n] = arr_copy[row-1][c+n]
            arr_copy[r-n+1][c+n] = temp

    for row in arr_copy:
        ans = min(ans, sum(row))

print(ans)
