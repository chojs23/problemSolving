from collections import deque

n, K = map(int, input().split())
q = deque()
move = [0] * 100001  # move 배열 👉 move[현재노드] = 이전 노드 (=부모노드)
dist = [0] * 100001  # dist 배열 👉 dist[현재 노드] = 걸리는 시간(초)
q.append(n)


def path(x):
    arr = []
    temp = x
    for _ in range(dist[x] + 1):
        arr.append(temp)
        temp = move[temp]
    print(" ".join(map(str, arr[::-1])))


def bfs():
    while q:
        x = q.popleft()
        if x == K:
            print(dist[x])
            path(x)
            return x
        for i in (x - 1, x + 1, x * 2):
            if 0 <= i <= 100000 and dist[i] == 0:
                q.append(i)
                dist[i] = dist[x] + 1
                move[i] = x


bfs()
