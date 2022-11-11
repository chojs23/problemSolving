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


def solution(arr):
    answer = [0, 0]
    length = len(arr)

    def compression(a, b, l):
        start = arr[a][b]

        for i in range(a, a + l):
            for j in range(b, b + l):
                if arr[i][j] != start:
                    l //= 2
                    compression(a, b, l)
                    compression(a, b + l, l)
                    compression(a + l, b, l)
                    compression(a + l, b + l, l)
                    return
        answer[start] += 1

    compression(0, 0, length)

    return answer


solution([[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]])
