from collections import deque,defaultdict
INF=10**9
def solution(n, wires):
    res = INF

    def bfs(wires):
        edges = defaultdict(list)
        cnt = 1
        for w in wires:
            a, b = w
            edges[a].append(b)
            edges[b].append(a)
        q = deque()
        q.append(1)
        visited = [0] * (n + 1)
        visited[1] = 1
        while q:
            u = q.popleft()
            for v in edges[u]:
                if not visited[v]:
                    q.append(v)
                    visited[v] = 1
                    cnt += 1
        return cnt

    for i in range(len(wires)):
        temp = wires[:i] + wires[i + 1 :]

        cnt = bfs(temp)
        if cnt >= n // 2:
            a, b = cnt, n - cnt
        else:
            a, b = n - cnt, cnt
        res = min(res, a - b)

    return res
