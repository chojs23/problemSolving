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

# ==========================================================


def find_video(start_n, k, map_dict):
    queue = deque()
    queue.append((start_n, float('inf')))
    visit_list = [-1] * N
    visit_list[start_n] = 1
    count = 0

    while queue:
        pop_node, min_dist = queue.popleft()
        for next_n, dist in map_dict[pop_node]:
            if visit_list[next_n] == 1:
                continue
            if min_dist > dist:
                queue.append((next_n, dist))
                if dist >= k:
                    count += 1
            else:
                if min_dist >= k:
                    count += 1
                    queue.append((next_n, min_dist))
            visit_list[next_n] = 1

    return count


N, Q = map(int, input().split())
map_dict = defaultdict(list)

for _ in range(N-1):
    p, q, r = map(int, input().split())
    map_dict[p-1].append((q-1, r))
    map_dict[q-1].append((p-1, r))

for _ in range(Q):
    k, v = map(int, input().split())
    print(find_video(v-1, k, map_dict))
