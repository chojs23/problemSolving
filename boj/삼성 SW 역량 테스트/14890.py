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


n, l = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(map(int, input().rstrip().split())))


def check(li):
    sw = [False for i in range(n)]
    for i in range(n - 1):
        if li[i] == li[i + 1]:
            continue
        if abs(li[i] - li[i + 1]) > 1:
            return False
        if li[i] > li[i + 1]:
            temp = li[i + 1]
            for j in range(i + 1, i + 1 + l):
                if 0 <= j < n:
                    if li[j] != temp:
                        return False
                    if sw[j] == True:
                        return False
                    sw[j] = True
                else:
                    return False
        else:
            temp = li[i]
            for j in range(i, i - l, -1):
                if 0 <= j < n:
                    if li[j] != temp:
                        return False
                    if sw[j] == True:
                        return False
                    sw[j] = True
                else:
                    return False
    return True


cnt = 0
for i in arr:
    if check(i):
        cnt += 1
for i in range(n):
    temp = []
    for j in range(n):
        temp.append(arr[j][i])
    if check(temp):
        cnt += 1
print(cnt)
