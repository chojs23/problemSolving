import sys
from collections import deque

input = sys.stdin.readline


N, M = map(int, input().split())

arr = []
q = deque()
inDegree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for i in range(M):
    arr.append(map(int, input().rstrip().split(" ")))

for win, lose in arr:
    inDegree[lose] += 1
    graph[win].append(lose)

for i in range(1, N + 1):
    if inDegree[i] == 0:
        q.append(i)

while q:
    cur = q.popleft()
    print(cur, end=" ")
    for lose in graph[cur]:
        inDegree[lose] -= 1
        if inDegree[lose] == 0:
            q.append(lose)
