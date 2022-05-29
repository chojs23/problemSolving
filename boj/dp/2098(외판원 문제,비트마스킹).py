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


n = int(input())
w = []

for i in range(n):
    w.append(list(map(int, input().split())))

# dp[cur][visited] = min(dp[cur][visited], dp[next][visited | (1 << next)] + graph[cur][next])
# 0001(2) = 1  => 0번 도시만을 거침
# 0011(2) = 3  => 0, 1 번 도시를 거침
# dp[cur][visit] = 현재 cur도시이며 방문현황은 visit과 같고, 아직 방문하지 않은 도시들을 모두 거쳐 다시 시작점으로 돌아가는데 드는 최소 비용
dp = [[INF] * (1 << n) for _ in range(n)]


def find(x, visited):
    if visited == (1 << n) - 1:
        if w[x][0]:
            return w[x][0]
        else:
            return INF

    if dp[x][visited] != INF:
        return dp[x][visited]

    for i in range(1, n):
        if not w[x][i]:
            continue
        if visited & (1 << i):
            continue

        dp[x][visited] = min(dp[x][visited], find(i, visited | (1 << i)) + w[x][i])

    return dp[x][visited]


print(find(0, 1))
