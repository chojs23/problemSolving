from collections import deque


def solution(places):
    answer = []
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

    def bfs(place, r, c):
        visited = [[False for _ in range(5)] for _ in range(5)]
        q = deque()
        visited[r][c] = True
        q.append((r, c, 0))
        while q:
            curr, curc, dis = q.popleft()
            if dis > 2:
                continue
            if dis != 0 and place[curr][curc] == "P":
                return
            for i in range(4):
                nx, ny = curr + dx[i], curc + dy[i]

                if nx < 0 or nx > 4 or ny < 0 or ny > 4:
                    continue
                if visited[nx][ny]:
                    continue
                if place[nx][ny] == "X":
                    continue

                visited[nx][ny] = True
                q.append((nx, ny, dis + 1))

        return True

    def check(place):
        for j in range(5):
            for k in range(5):
                if place[j][k] == "P":
                    if not bfs(place, j, k):
                        return False
        return True

    for place in places:
        if check(place):
            answer.append(1)
        else:
            answer.append(0)

    return answer
