from copy import copy, deepcopy
from math import sqrt
import sys
from collections import defaultdict, deque
from itertools import combinations, permutations
import heapq
import bisect

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

input = sys.stdin.readline
INF = sys.maxsize

# ===========================================================
dr, dc = [-1, 0, 0, 1], [0, -1, 1, 0]

n, m, fuel = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

startPos = list(map(int, input().split()))

passenger = [list(map(int, input().split())) for _ in range(m)]


def bfs(s_x, s_y):
    visited = [[-1] * n for _ in range(n)]
    queue = deque()
    queue.append((s_x, s_y))
    visited[s_x][s_y] = 0

    while queue:
        pop_x, pop_y = queue.popleft()

        for i in range(4):
            n_x, n_y = pop_x + dr[i], pop_y + dc[i]

            if n_x < 0 or n_x >= n or n_y < 0 or n_y >= n:
                continue
            if arr[n_x][n_y] == 1 or visited[n_x][n_y] != -1:
                continue

            visited[n_x][n_y] = visited[pop_x][pop_y] + 1
            queue.append((n_x, n_y))

    return visited


def check_dist(visited: list, passenger: list):
    i = 0
    for p_x, p_y, a_x, a_y in passenger:
        passenger[i].append(visited[p_x - 1][p_y - 1])
        i += 1

    passenger.sort(key=lambda x: (-x[4], -x[0], -x[1]))


def solve(s_x, s_y):
    global fuel
    while passenger:
        visitied = bfs(s_x - 1, s_y - 1)
        check_dist(visitied, passenger)
        p_x, p_y, a_x, a_y, dist = passenger.pop()

        for temp in passenger:
            temp.pop()

        visitied = bfs(p_x - 1, p_y - 1)
        dist2 = visitied[a_x - 1][a_y - 1]
        s_x, s_y = a_x, a_y

        if dist == -1 or dist2 == -1:
            print(-1)
            return

        fuel -= dist
        if fuel < 0:
            break

        fuel -= dist2
        if fuel < 0:
            break

        fuel += dist2 * 2

    if fuel < 0:
        print(-1)
    else:
        print(fuel)


solve(startPos[0], startPos[1])
