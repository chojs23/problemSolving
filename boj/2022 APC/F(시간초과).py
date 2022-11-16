import collections
import itertools
from copy import copy, deepcopy
import math
import sys
from collections import defaultdict, deque
from itertools import combinations, permutations
import heapq
import bisect
import math

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

input = sys.stdin.readline
INF = sys.maxsize

# ==========================================================


def get_smallest_node(distance):
    min_value = INF
    index = 0
    for n in range(len(nodes) - 1):
        i, j = nodes[n]
        if distance[i][j] < min_value and not visited[i][j]:
            min_value = distance[i][j]
            index = (i, j)
    return index


def dijkstra(start):
    distance = [[INF] * N for _ in range(N)]
    # 시작 노드
    distance[start[0]][start[1]] = 0
    visited[start[0]][start[1]] = 1
    # 출발노드와 인접노드에 대해 최단거리 테이블 갱신
    for j in edges2[start]:
        distance[j[0]][j[1]] = j[2]
    # 모든 노드에 대해 반복
    for _ in range(len(nodes) - 1):
        # 현재 최단거리가 가장 짧은 노드를 꺼내서 방문처리
        now = get_smallest_node(distance)
        if now == 0:
            continue
        visited[now[0]][now[1]] = 1
        # 선택된 노드와 연결된 다른 노드를 확인
        for j in edges2[now]:
            # 선택된 노드를 통해 가는 비용을 다시 계산
            # 선택된 노드의 비용 + 연결된 노드로 가는 비용
            cost = distance[now[0]][now[1]] + j[2]
            # 선택된 노드를 거쳐서 가는 비용이 더 짧은 경우
            if cost < distance[j[0]][j[1]]:
                distance[j[0]][j[1]] = cost  # 최단거리 테이블 갱신
    return distance


pdr, pdc = [-1, 1, 0, 0, -1, -1, 1, 1], [0, 0, -1, 1, -1, 1, -1, 1]


def getPossibleP(r, c):
    for i in range(8):
        nr, nc = r + pdr[i], c + pdc[i]

        if 0 <= nr < N and 0 <= nc < N and board[nr][nc] != "0":
            edges2[(r, c)].append([nr, nc, 1])


bdr, bdc = [-1, -1, 1, 1], [-1, 1, -1, 1]


def getPossibleB(r, c):
    for i in range(4):
        cnt = 1
        nr, nc = r + bdr[i], c + bdc[i]
        while 0 <= nr < N and 0 <= nc < N:

            if board[nr][nc] != "0":
                edges2[(r, c)].append([nr, nc, cnt])
                break

            nr, nc = nr + bdr[i], nc + bdc[i]
            cnt += 1


def getPossibleQ(r, c):
    for i in range(8):
        cnt = 1
        nr, nc = r + pdr[i], c + pdc[i]
        while 0 <= nr < N and 0 <= nc < N:
            if board[nr][nc] != "0":
                edges2[(r, c)].append([nr, nc, cnt])
                break
            nr, nc = nr + pdr[i], nc + pdc[i]
            cnt += 1


ndr, ndc = [-1, -2, -2, -1, 1, 2, 2, 1], [-2, -1, 1, 2, -2, -1, 1, 2]


def getPossibleN(r, c):
    for i in range(8):
        nr, nc = r + ndr[i], c + ndc[i]

        if 0 <= nr < N and 0 <= nc < N and board[nr][nc] != "0":
            edges2[(r, c)].append([nr, nc, 2])


def getPossibleR(r, c):
    for i in range(4):
        cnt = 1
        nr, nc = r + pdr[i], c + pdc[i]
        while 0 <= nr < N and 0 <= nc < N:
            if board[nr][nc] != "0":
                edges2[(r, c)].append([nr, nc, cnt])
                break
            nr, nc = nr + pdr[i], nc + pdc[i]
            cnt += 1


N = int(input())
node_visited = [[0] * N for _ in range(N)]
board = [list(input().split()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
edges2 = defaultdict(list)
nodes = []
for i, r in enumerate(board):
    for j, c in enumerate(r):
        if c == "P":
            P = (i, j)
            nodes.append((i, j))
            getPossibleP(i, j)
        elif c == "B":
            getPossibleB(i, j)
            nodes.append((i, j))
        elif c == "Q":
            getPossibleQ(i, j)
            nodes.append((i, j))
        elif c == "N":
            getPossibleN(i, j)
            nodes.append((i, j))
        elif c == "R":
            getPossibleR(i, j)
            nodes.append((i, j))
        elif c == "K":
            K = (i, j)
            nodes.append(K)


distance: list[list[int]] = dijkstra(P)
# print(distance)

print(distance[K[0]][K[1]]) if distance[K[0]][K[1]] != INF else print(-1)
