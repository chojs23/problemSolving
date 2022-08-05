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

n, m = map(int, input().split())


witness = set(input().split()[1:])

party_list = []
possible_list = []

for _ in range(m):
    party_list.append(set(sys.stdin.readline().rstrip().split()[1:]))
    possible_list.append(1)

for i in range(m):
    for i, party in enumerate(party_list):
        if witness.intersection(party):
            possible_list[i] = 0
            witness = witness.union(party)

print(sum(possible_list))
