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

n = int(input())
teacher = 0
arr = list(list(input().split()) for _ in range(n))
for a in arr:
    teacher += a.count('T')

answer = False


def bfs(r, c):
    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]

        while 0 <= nr < n and 0 <= nc < n and arr[nr][nc] != 'O':
            if arr[nr][nc] == 'S':
                return False
            else:
                nr += dr[i]
                nc += dc[i]
    return True


def dfs(count):
    global answer
    if count == 3:
        cnt = 0
        for i in range(n):
            for j in range(n):
                if arr[i][j] == 'T':
                    if bfs(i, j):
                        cnt += 1
        if cnt == teacher:
            answer = True
        return

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'X':
                arr[i][j] = 'O'
                count += 1
                dfs(count)
                arr[i][j] = 'X'
                count -= 1


dfs(0)
print('YES') if answer else print('NO')
