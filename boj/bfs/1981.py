import sys
from collections import deque
from itertools import permutations

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

input = sys.stdin.readline


n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))


def bfs(r, c, _min, _max):
    if (arr[r][c] < _min) or (_max < arr[r][c]):
        return False
    q = deque()
    q.append((r, c))
    visit = [[False] * n for _ in range(n)]
    visit[r][c] = True
    while q:
        cur_r, cur_c = q.popleft()

        if cur_r == n - 1 and cur_c == n - 1:
            return True

        for i in range(4):
            nr, nc = cur_r + dr[i], cur_c + dc[i]

            if (
                0 <= nr < n
                and 0 <= nc < n
                and visit[nr][nc] == False
                and _min <= arr[nr][nc]
                and _max >= arr[nr][nc]
            ):
                q.append((nr, nc))
                visit[nr][nc] = True
    return False


left = right = 0
limit = max(map(max, arr))  # 배열의 원소의 최댓값 (left, right는 이 이상 커질 수 없다)
answer = sys.maxsize
while (left <= limit) and (right <= limit):
    if bfs(0, 0, left, right):  # 목적지에 도착했다면 (최대-최소)를 줄여본다.
        answer = min(answer, right - left)
        left += 1
    else:  # 목적지에 도달하지 못했다면 범위를 늘려주어야 한다.
        right += 1

print(answer)
