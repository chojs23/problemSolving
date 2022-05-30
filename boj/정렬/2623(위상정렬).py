from copy import copy, deepcopy
from math import sqrt
import sys
from collections import defaultdict, deque
from itertools import permutations
import heapq

dr, dc = [-1, 1, 0, 0], [0, 0, 1, -1]

input = sys.stdin.readline
INF = sys.maxsize

# ===========================================================


n, m = map(int, input().split())


inDegree = [0] * (n + 1)
graph = [[] for i in range(n + 1)]

for i in range(m):
    pd = list(map(int, input().split()))

    for s in range(1, pd[0]):
        graph[pd[s]].append(pd[s + 1])  # 노드(s) -> 노드(s+1)
        inDegree[pd[s + 1]] += 1

q = deque()
ans = []
for i in range(1, n + 1):
    if inDegree[i] == 0:
        q.append(i)  # 진입차수가 0인 노드 넣기

while q:
    cur = q.popleft()
    ans.append(cur)

    for i in graph[cur]:
        inDegree[i] -= 1

        if inDegree[i] == 0:
            q.append(i)

if len(ans) == n:
    for i in ans:
        print(i)
else:
    print(0)
