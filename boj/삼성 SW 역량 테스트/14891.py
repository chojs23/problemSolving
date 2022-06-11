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


def rotation(n, d):
    isRotate = [False for i in range(4)]
    direction = [0 for i in range(4)]
    isRotate[n] = True
    direction[n] = d
    tempn = n
    tempd = d
    for i in range(n + 1, 4):
        if s[tempn][2] != s[i][6]:
            isRotate[i] = True
            tempd = -tempd
            direction[i] = tempd
            tempn = i
        else:
            break
    tempn = n
    tempd = d
    for i in range(n - 1, -1, -1):
        if s[tempn][6] != s[i][2]:
            isRotate[i] = True
            tempd = -tempd
            direction[i] = tempd
            tempn = i
        else:
            break
    for i in range(4):
        if isRotate[i]:
            if direction[i] == 1:
                temp = s[i].pop()
                s[i] = [temp] + s[i]
            else:
                temp = s[i][0]
                del s[i][0]
                s[i].append(temp)


s = []
r = []
for i in range(4):
    s.append(list(input().strip()))
k = int(input())
for i in range(k):
    a, b = map(int, input().split())
    r.append([a - 1, b])
for n, d in r:
    rotation(n, d)
result = 0
for i in range(4):
    if s[i][0] == "1":
        result += 2**i
print(result)
