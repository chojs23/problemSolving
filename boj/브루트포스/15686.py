from copy import copy, deepcopy
import sys
from collections import deque
from itertools import permutations
import heapq

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

input = sys.stdin.readline

# ===========================================================

from itertools import combinations

n, m = map(int, input().split())
maps = []
for i in range(n):
    maps.append(list(map(int, input().split())))

home = []
chicken = []
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            home.append((i, j))
        elif maps[i][j] == 2:
            chicken.append((i, j))

pick_chicken = list(combinations(chicken, m))
result = [0] * len(pick_chicken)

for i in home:
    for j in range(len(pick_chicken)):
        a = 100
        for k in pick_chicken[j]:
            temp = abs(i[0] - k[0]) + abs(i[1] - k[1])
            a = min(a, temp)
        result[j] += a

print(min(result))
