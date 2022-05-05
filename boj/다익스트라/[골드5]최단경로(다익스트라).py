import collections
import heapq
import sys

input = sys.stdin.readline
INF = 20000 * 300000
V, E = map(int, input().split())

K = int(input())

edges = collections.defaultdict(list)

for _ in range(E):
    u, v, w = map(int, input().split())
    edges[u].append((w, v))

result = ["INF"] * (V + 1)
result[K] = 0
minHeap = [(0, K)]

visit = set()

while minHeap:
    w1, n1 = heapq.heappop(minHeap)

    if n1 in visit:
        continue
    visit.add(n1)
    result[n1] = w1
    for w2, n2 in edges[n1]:
        if n2 not in visit:
            heapq.heappush(minHeap, (w1 + w2, n2))


for i in range(1, V + 1):
    print(result[i])
