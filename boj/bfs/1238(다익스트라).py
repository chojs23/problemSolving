import collections
import heapq
import sys

input = sys.stdin.readline
inf = 10000 * 1001
N, M, X = map(int, input().split())

edges = [[] for _ in range(M + 1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    edges[u].append((w, v))

heap = [(0, X)]

fromX = [inf] * (N + 1)

fromX[X] = 0
toX = []
visit = set()

while heap:
    w1, n1 = heapq.heappop(heap)

    if n1 in visit:
        continue
    visit.add(n1)
    fromX[n1] = w1
    for w2, n2 in edges[n1]:
        if n2 not in visit:
            heapq.heappush(heap, (w1 + w2, n2))

for i in range(1, N + 1):
    heap = [(0, i)]
    visit.clear()
    temp = [inf] * (N + 1)
    temp[i] = 0

    while heap:
        w1, n1 = heapq.heappop(heap)

        if n1 in visit:
            continue
        visit.add(n1)
        temp[n1] = w1
        for w2, n2 in edges[n1]:
            if n2 not in visit:
                heapq.heappush(heap, (w1 + w2, n2))
    toX.append(temp[:])
res = 0

for i in range(1, N + 1):
    res = max(res, toX[i - 1][X] + fromX[i])

print(res)
print(toX)
print(fromX)
