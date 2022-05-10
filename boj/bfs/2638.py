from copy import copy, deepcopy
import sys
from collections import deque
from itertools import permutations
import heapq

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

input = sys.stdin.readline

# ===========================================================

n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().rstrip().split())))


def bfs():
    q = deque()
    q.append((0, 0))

    visit = [[False] * m for _ in range(n)]
    visit[0][0] = True

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < n and 0 <= nc < m and not visit[nr][nc]:

                if arr[nr][nc] >= 1:
                    arr[nr][nc] += 1
                else:
                    visit[nr][nc] = True
                    q.append((nr, nc))


ans = 0
while True:
    bfs()
    check = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] >= 3:
                arr[i][j] = 0

                check = 1
            elif arr[i][j] == 2:
                arr[i][j] = 1

    if check:
        ans += 1
    else:
        break

print(ans)
