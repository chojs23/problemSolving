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
distance = [inf for i in range(N + 1)]


for i in range(M):
    s, e, w = map(int, input().split())
    arr[s].append((e, w))

start, end = map(int, input().split())

path = [[] for i in range(N + 1)]
path[start].append(start)


def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))

    distance[start] = 0
    while heap:

        dist, now = heapq.heappop(heap)

        if distance[now] < dist:
            continue

        for next, w in arr[now]:
            cost = dist + w

            if distance[next] > cost:
                distance[next] = cost
                heapq.heappush(heap, (cost, next))
                path[next] = []
                for p in path[now]:
                    path[next].append(p)
                path[next].append(next)


dijkstra(start)

print(distance[end])
print(len(path[end]))
print(" ".join(map(str, path[end])))
