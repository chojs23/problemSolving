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


n, k = map(int, input().split())
visited = [0] * 100001


def bfs(n):
    ans_count = 0
    ans_way = 0
    q = deque([n])

    visited[n] = 0
    while q:
        x = q.popleft()
        count = visited[x]

        if x == k:
            ans_count = count
            ans_way += 1
            continue

        for nx in [x - 1, x + 1, 2 * x]:
            if 0 <= nx < 100001:
                if visited[nx] == 0 or visited[nx] == visited[x] + 1:
                    q.append(nx)
                    visited[nx] = count + 1

    return ans_count, ans_way


ans_cnt, ans_way = bfs(n)

print(ans_cnt)
print(ans_way)
