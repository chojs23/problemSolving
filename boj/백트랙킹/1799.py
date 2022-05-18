import sys

# check : 현재 좌표 (x, y)에서 이전에 놓은 비숍에 영향을 받는지 아닌지를 체크하는 함수
def check(x, y):
    # 현재 칸이 비숍을 영향을 받으면 놓을 수 없으므로 False 리턴
    if temp[x][y]:
        return False
    # 그렇지 않다면 놓을 수 있으므로 True 리턴
    return True


# set : 현재 (x, y)에서 비숍을 놓거나 놓지 않는 함수. 이 때 num은 1 또는 -1로 놓는 경우는 1,놓았다가 다시 빼는 경우는 -1로 나타낸다
def set(x, y, num):
    global blank
    for i in range(n):
        # 좌상 대각선
        nx, ny = x - i, y - i
        if 0 <= nx < n and 0 <= ny < n:
            temp[nx][ny] += num
        # 좌하 대각선
        nx, ny = x + i, y - i
        if 0 <= nx < n and 0 <= ny < n:
            temp[nx][ny] += num
        # 우상 대각선
        nx, ny = x - i, y + i
        if 0 <= nx < n and 0 <= ny < n:
            temp[nx][ny] += num
        # 우하 대각선
        nx, ny = x + i, y + i
        if 0 <= nx < n and 0 <= ny < n:
            temp[nx][ny] += num


# backtracking : 현재 idx번째 점에서 cnt개의 비숍을 놓는 함수
def backtracking(idx, cnt):
    global ans
    # Base Case : 모든 점을 탐색 후 정답 갱신
    if idx >= len(grid):
        ans = max(ans, cnt)
        return
    x, y = grid[idx]
    # 현재 칸에 놓을 수 있다면 backtracking
    if check(x, y):
        set(x, y, 1)
        backtracking(idx + 1, cnt + 1)
        set(x, y, -1)
        backtracking(idx + 1, cnt)
    # 놓을 수 없다면 다음 칸으로 이동
    else:
        backtracking(idx + 1, cnt)


# 입력부
n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# temp : 비숍의 영향에 있는지 아닌지를 체크하는 2차원 배열, 0이면 영향에 있지 않고 1이면 영향에 있다
temp = [[0] * n for _ in range(n)]

# grid : 놓을 수 있는 좌표의 list
grid = []
ans = 0
for i in range(n):
    for j in range(n):
        if arr[i][j]:
            # 흰칸(검은칸)만 담음
            if (i + j) % 2 == 0:
                grid.append((i, j))

# 흰칸(검은칸)에 대해서만 백트래킹
backtracking(0, 0)
res1 = ans

temp = [[0] * n for _ in range(n)]
grid = []
ans = 0
for i in range(n):
    for j in range(n):
        if arr[i][j]:
            # 검은칸(흰칸)만 담음
            if (i + j) % 2 == 1:
                grid.append((i, j))

# 검은칸(흰칸)에 대해서만 백트래킹
backtracking(0, 0)
res2 = ans

# 두 경우를 더하여 정답 출력
print(res1 + res2)
