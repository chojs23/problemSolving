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

# ==========================================================
INF = 1000000000
n = int(input())
m = int(input())

road = [[INF] * n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())

    road[a - 1][b - 1] = min(road[a - 1][b - 1], c)


for i in range(n):
    for j in range(n):
        for k in range(n):
            if j != k and road[j][k] > road[j][i] + road[i][k]:
                road[j][k] = road[j][i] + road[i][k]

for i in range(n):
    for j in range(n):
        if road[i][j] == INF:
            road[i][j] = 0

for i in road:
    for j in i:
        if j == INF:
            print(0, end=" ")
        else:
            print(j, end=" ")
    print()
