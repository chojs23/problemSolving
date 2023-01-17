import collections
import itertools
from copy import copy, deepcopy
import math
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


def bf(start):
    dist = [INF] * (N + 1)
    dist[start] = 0
    for i in range(N):
        for cur, next, w in edges:
            if dist[next] > dist[cur] + w:
                dist[next] = dist[cur] + w
                if i == N - 1:
                    return True
    return False


T = int(input())

for _ in range(T):
    N, M, W = map(int, input().split())
    edges = []
    for _ in range(M):
        S, E, T = map(int, input().split())
        edges.append((S, E, T))
        edges.append((E, S, T))
    for _ in range(W):
        S, E, T = map(int, input().split())
        edges.append((S, E, -T))

    if bf(1):
        print("YES")
    else:
        print("NO")
