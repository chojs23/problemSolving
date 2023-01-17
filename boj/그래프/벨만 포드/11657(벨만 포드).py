from copy import copy, deepcopy
import sys
from collections import defaultdict, deque
from itertools import permutations
import heapq

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

input = sys.stdin.readline
INF = sys.maxsize
# ===========================================================

n, m = map(int, input().split())

edges = []
dist = [INF] * (n + 1)

for _ in range(m):
    start, end, cost = map(int, input().split())
    edges.append((start, end, cost))

dist = [INF] * (n + 1)

# 다익스트라 음수 간선 있으면  벨만 포드 알고리즘
# 벨만 포드 알고리즘
def bf(start):
    dist[start] = 0  # 시작 노드에 대해서 거리를 0으로 초기화
    for i in range(n):  # 정점 수만큼 반복
        for j in range(m):  # 매 반복 마다 모든 간선 확인
            node = edges[j][0]  # 현재 노드 받아오기
            next_node = edges[j][1]  # 다음 노드 받아오기
            cost = edges[j][2]  # 가중치 받아오기
            # 현재 간선을 걸쳐 다른 노드로 이동하는 거리가 더 짧은 경우
            if dist[node] != INF and dist[next_node] > dist[node] + cost:
                dist[next_node] = dist[node] + cost
                # n번째 라운드에서도 값이 갱신된다면 음수 순환이 존재
                if i == n - 1:  # n-1번 이후 반복에도 값이 갱신되면 음수 순환 존재
                    return True
    return False


negative_cycle = bf(1)

if negative_cycle:
    print("-1")
else:
    for i in range(2, n + 1):
        if dist[i] == INF:
            print("-1")
        else:
            print(dist[i])
