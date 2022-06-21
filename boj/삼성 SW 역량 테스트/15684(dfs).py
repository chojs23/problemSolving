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


inf = 5
n, m, h = map(int, input().split())
s = [[0] * (n + 1) for i in range(h + 1)]
result = inf


def check():
    for i in range(1, n + 1):
        temp = i
        for j in range(1, h + 1):
            if s[j][temp] == 1:
                temp += 1
            elif s[j][temp - 1] == 1:
                temp -= 1
        if temp != i:
            return False
    return True


def dfs(num, cnt):
    global result
    if result != 5:
        return
    if num == cnt:
        if check():
            result = cnt
        return
    for j in range(1, n):
        for i in range(1, h + 1):
            if s[i][j - 1] == 0 and s[i][j + 1] == 0 and s[i][j] == 0:
                s[i][j] = 1
                dfs(num, cnt + 1)
                s[i][j] = 0
                # while i < h:
                #     if s[i][j - 1] or s[i][j + 1]:
                #         break
                #     i += 1


for i in range(m):
    a, b = map(int, input().split())
    s[a][b] = 1
for i in range(4):
    dfs(i, 0)
    if result != inf:
        print(result)
        break
if result == inf:
    print(-1)
