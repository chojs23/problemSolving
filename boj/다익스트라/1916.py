import sys
from collections import deque
from itertools import permutations
import heapq

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

input = sys.stdin.readline

# ===========================================================
inf = 100000000

N = int(input())
M = int(input())
arr = [[] for _ in range(N + 1)]
dp = [inf for i in range(N + 1)]


for i in range(M):
    s, e, w = map(int, input().split())
    arr[s].append((e, w))

start, end = map(int, input().split())


def dijkstra(start):
    dp[start] = 0
    heap = []
    heapq.heappush(heap, [0, start])
    while heap:
        w, n = heapq.heappop(heap)
        if dp[n] < w:
            continue
        for n_n, weight in arr[n]:
            n_w = w + weight
            if dp[n_n] > n_w:
                dp[n_n] = n_w
                heapq.heappush(heap, [n_w, n_n])


dijkstra(start)
print(dp[end])
