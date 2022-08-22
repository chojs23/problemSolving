from collections import deque


def bfs(dest, graph, n):
    q = deque()
    visited = [-1 for _ in range(n)]
    q.append(dest)
    cnt = 0
    while q:
        cnt += 1
        length = len(q)
        for i in range(length):
            a = q.popleft()
            for nxt in graph[a]:
                if visited[nxt] > 0:
                    continue
                q.append(nxt)
                visited[nxt] = cnt
    return visited


def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for _ in range(n)]
    for r in roads:
        a, b = r
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

    ret = bfs(destination-1, graph, n)
    # print(ret)
    ret[destination-1] = 0
    for s in sources:
        answer.append(ret[s-1])
    return answer
