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
switch = list(map(int, input().split()))

m = int(input())

oper = []

for _ in range(m):
    a, b = map(int, input().split())
    oper.append([a, b])


def boyDo(num):
    temp = num-1
    while temp < len(switch):
        if switch[temp] == 0:
            switch[temp] = 1
        else:
            switch[temp] = 0

        temp += num


stk = []


def palindromeIdx(num):
    l, r = num-1, num+1
    ret = (-1, -1)
    while l >= 0 and r < len(switch):
        if switch[l] == switch[r]:
            ret = (l, r)
            l -= 1
            r += 1
        else:
            return ret
    return ret


def girlDo(num):

    l, r = palindromeIdx(num-1)

    if l == -1 and r == -1:
        if switch[num-1] == 0:
            switch[num-1] = 1
        else:
            switch[num-1] = 0
        return

    for i in range(l, r+1):
        if switch[i] == 0:
            switch[i] = 1
        else:
            switch[i] = 0


for o in oper:
    a, b = o

    if a == 1:
        boyDo(b)
    else:
        girlDo(b)

count = 0
while count < len(switch):

    print(switch[count], end=" ")
    if count % 20 == 19:
        print()
    count += 1
