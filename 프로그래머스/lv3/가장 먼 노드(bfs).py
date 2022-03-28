from collections import defaultdict
from collections import deque


def solution(n, edge):
    answer = 0
    graph = defaultdict(list)
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    q = deque()
    q.append(1)

    visited = defaultdict(int)
    visited[1] = 1
    cnt = 0
    # print(graph)
    while q:
        cnt = 0
        # print('============')
        for i in range(len(q)):
            cur = q.popleft()
            cnt += 1
            for j in graph[cur]:
                if visited[j] != 1:
                    visited[j] = 1
                    q.append(j)
        # print(visited)

    # print(cnt)
    return cnt
