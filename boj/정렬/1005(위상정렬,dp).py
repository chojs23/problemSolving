from copy import copy, deepcopy
import sys
from collections import defaultdict, deque
from itertools import permutations
import heapq

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

input = sys.stdin.readline

# ===========================================================

T = int(input())


for _ in range(T):
    N, K = map(int, input().split())

    time = [0] + list(map(int, input().rstrip().split()))
    inDegree = [0] * (N + 1)
    tree = [[] for _ in range(N + 1)]

    for i in range(K):
        start, end = map(int, input().split())
        tree[start].append(end)
        inDegree[end] += 1

    W = int(input())

    dp = [0] * (N + 1)

    q = deque()

    for i in range(1, N + 1):
        if inDegree[i] == 0:
            q.append(i)
            dp[i] = time[i]

    while q:
        a = q.popleft()

        for i in tree[a]:
            inDegree[i] -= 1
            dp[i] = max(dp[a] + time[i], dp[i])
            if inDegree[i] == 0:
                q.append(i)

    print(dp[W])
