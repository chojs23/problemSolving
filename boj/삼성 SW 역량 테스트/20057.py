from copy import copy, deepcopy
from math import sqrt
import sys
from collections import defaultdict, deque
from itertools import combinations, permutations
import heapq
import bisect

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

input = sys.stdin.readline
INF = sys.maxsize

# ===========================================================


N = int(input())

sand = [list(map(int, input().split())) for _ in range(N)]

s_x, s_y = N // 2, N // 2  # 시작좌표(x좌표)
ans = 0  # out_sand

left = [
    (1, 1, 0.01),
    (-1, 1, 0.01),
    (1, 0, 0.07),
    (-1, 0, 0.07),
    (1, -1, 0.1),
    (-1, -1, 0.1),
    (2, 0, 0.02),
    (-2, 0, 0.02),
    (0, -2, 0.05),
    (0, -1, 0),
]
right = [(x, -y, z) for x, y, z in left]
down = [(-y, x, z) for x, y, z in left]
up = [(y, x, z) for x, y, z in left]

# 모래 계산하는 함수
def recount(time, dx, dy, direction):
    global ans, s_x, s_y

    # y좌표 계산 & x좌표 갱신
    for _ in range(time):
        s_x += dx
        s_y += dy
        if s_y < 0:  # 범위 밖이면 stop
            break

        # 3. a, out_sand
        total = 0  # a 구하기 위한 변수
        for dx, dy, z in direction:
            nx = s_x + dx
            ny = s_y + dy
            if z == 0:  # a(나머지)
                new_sand = sand[s_x][s_y] - total
            else:  # 비율
                new_sand = int(sand[s_x][s_y] * z)
                total += new_sand

            if 0 <= nx < N and 0 <= ny < N:  # 인덱스 범위이면 값 갱신
                sand[nx][ny] += new_sand
            else:  # 범위 밖이면 ans 카운트
                ans += new_sand


# 1.토네이도 회전 방향(y위치)
for i in range(1, N + 1):
    if i % 2:
        recount(i, 0, -1, left)
        recount(i, 1, 0, down)
    else:
        recount(i, 0, 1, right)
        recount(i, -1, 0, up)

print(ans)
