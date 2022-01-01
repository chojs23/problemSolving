import sys
import copy

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]  # 그래프 생성
graph_copy = copy.deepcopy(graph)  # deepcopy 깊은복사 vs 얕은복사 정리

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]  # 상하좌우 이동

safe = 0


def virus(x, y, sel_graph):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if sel_graph[nx][ny] == 0:
                sel_graph[nx][ny] = 2
                virus(nx, ny, sel_graph)


def select(start, count):
    global safe
    if count == 3:
        sel_graph = copy.deepcopy(graph_copy)
        for i in range(n):
            for j in range(m):
                if sel_graph[i][j] == 2:
                    virus(i, j, sel_graph)
        safe_count = sum(_.count(0) for _ in sel_graph)
        safe = max(safe, safe_count)
        return
    else:
        for i in range(start, n * m):
            r = i // m
            c = i % m
            if graph_copy[r][c] == 0:
                graph_copy[r][c] = 1
                select(i, count + 1)
                graph_copy[r][c] = 0


select(0, 0)

print(safe)
