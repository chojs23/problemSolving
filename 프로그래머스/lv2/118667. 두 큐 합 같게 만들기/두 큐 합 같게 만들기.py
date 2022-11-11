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
INF = sys.maxsize

# ==========================================================

sys.setrecursionlimit(10**9)


def solution(queue1, queue2):
    answer = -1
    length = len(queue1)
    total = sum(queue1) + sum(queue2)
    if total % 2 != 0:
        return -1

    target = total // 2
    q1 = deque(queue1)
    q2 = deque(queue2)

    cnt = 0
    cnt1 = 0
    cnt2 = 0
    sumA = sum(queue1)

    while True:
        if sumA == target:
            answer = cnt
            break
        if cnt1 > length and cnt2 > length:
            return -1
        if sumA > total - sumA:
            temp = q1.popleft()
            sumA -= temp
            q2.append(temp)
            cnt += 1
            cnt1 += 1
        else:
            temp = q2.popleft()
            sumA += temp
            q1.append(temp)
            cnt += 1
            cnt2 += 1

    return answer


