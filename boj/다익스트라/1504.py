import sys
from collections import deque
from itertools import permutations
import heapq

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

input = sys.stdin.readline

# ===========================================================
INF = 10**9
N, E = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for i in range(E):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
    graph[e].append((s, w))

v1, v2 = map(int, input().split())


def dijkstra(start):
    q = []
    distance = [INF] * (N + 1)

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for next, next_cost in graph[now]:
            cost = next_cost + dist

            if distance[next] > cost:
                distance[next] = cost
                heapq.heappush(q, (cost, next))

    return distance


dis_start = dijkstra(1)
dis_v1 = dijkstra(v1)
dis_v2 = dijkstra(v2)


res = min(
    dis_start[v1] + dis_v1[v2] + dis_v2[N], dis_start[v2] + dis_v2[v1] + dis_v1[N]
)

print(res) if res < INF else print(-1)
