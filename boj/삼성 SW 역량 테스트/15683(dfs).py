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


n, m = map(int, input().split())

arr = []

dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]


def fill(r, c, arr, d):
    for i in d:
        nr, nc = r, c
        while True:
            nr += dr[i]
            nc += dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if arr[nr][nc] == 6:
                    break
                elif arr[nr][nc] == 0:
                    arr[nr][nc] = "#"
            else:
                break


def dfs(arr, cnt):
    global result
    temp = deepcopy(arr)
    if cnt == cctv_cnt:
        num = 0
        for i in range(n):
            num += temp[i].count(0)
        result = min(result, num)
        return
    x, y, cctv = q[cnt]
    for i in direction[cctv]:
        fill(x, y, temp, i)
        dfs(temp, cnt + 1)
        temp = deepcopy(arr)


direction = [
    [],
    [[0], [1], [2], [3]],
    [[0, 1], [2, 3]],
    [[3, 0], [0, 2], [2, 1], [1, 3]],
    [[1, 3, 0], [3, 0, 2], [0, 2, 1], [2, 1, 3]],
    [[0, 1, 2, 3]],
]

cctv_cnt = 0
result = 100000000
q = []

for i in range(n):
    a = list(map(int, input().split()))
    arr.append(a)
    for j in range(len(a)):
        if a[j] != 0 and a[j] != 6:
            q.append([i, j, a[j]])
            cctv_cnt += 1

dfs(arr, 0)
print(result)
