from copy import copy, deepcopy
import sys
from collections import deque
from itertools import permutations
import heapq

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

input = sys.stdin.readline

# ===========================================================

# Prim Algorithm

V, E = map(int, input().split())
Elist = [[] for _ in range(V + 1)]
visited = [False] * (V + 1)
heap = [[0, 1]]  # weight,start
for _ in range(E):
    s, e, w = map(int, input().split())
    Elist[s].append([w, e])
    Elist[e].append([w, s])

ans = 0
cnt = 0
while heap:
    # if cnt == V:
    # break
    w, s = heapq.heappop(heap)
    if not visited[s]:
        visited[s] = True
        ans += w
        cnt += 1
        for i in Elist[s]:
            heapq.heappush(heap, i)

print(ans)


# Kruskal

V, E = map(int, input().split())
Vroot = [i for i in range(V + 1)]
Elist = []
for _ in range(E):
    Elist.append(list(map(int, input().split())))

Elist.sort(key=lambda x: x[2])


def find(x):
    if x != Vroot[x]:
        Vroot[x] = find(Vroot[x])
    return Vroot[x]


answer = 0
for s, e, w in Elist:
    sRoot = find(s)
    eRoot = find(e)
    if sRoot != eRoot:
        if sRoot > eRoot:
            Vroot[sRoot] = eRoot
        else:
            Vroot[eRoot] = sRoot
        answer += w

print(answer)
