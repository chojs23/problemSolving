from copy import copy, deepcopy
import sys
from collections import deque
from itertools import permutations
import heapq

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

input = sys.stdin.readline

# ===========================================================


N = int(input())

mindp = [[0] * 3 for _ in range(2)]
maxdp = [[0] * 3 for _ in range(2)]


for i in range(N):
    temp = list(map(int, input().split()))
    maxdp[1][0] = max(maxdp[0][1], maxdp[0][0]) + temp[0]
    maxdp[1][1] = max(maxdp[0][1], maxdp[0][0], maxdp[0][2]) + temp[1]
    maxdp[1][2] = max(maxdp[0][1], maxdp[0][2]) + temp[2]

    mindp[1][0] = min(mindp[0][1], mindp[0][0]) + temp[0]
    mindp[1][1] = min(mindp[0][1], mindp[0][0], mindp[0][2]) + temp[1]
    mindp[1][2] = min(mindp[0][1], mindp[0][2]) + temp[2]

    maxdp[0][0], maxdp[0][1], maxdp[0][2] = maxdp[1][0], maxdp[1][1], maxdp[1][2]
    mindp[0][0], mindp[0][1], mindp[0][2] = mindp[1][0], mindp[1][1], mindp[1][2]

print(max(maxdp[0]), min(mindp[0]))
