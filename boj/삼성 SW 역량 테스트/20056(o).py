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

n, m, k = map(int, input().split())

fireball = [list(map(int, input().split())) for _ in range(m)]

dir = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
arr = [[deque() for _ in range(n)] for _ in range(n)]

for f in fireball:
    r, c, m, s, d = f

    arr[r - 1][c - 1].append([m, s, d])


def calculate_pos(x):
    if x < 0:
        if x > -n:
            answer = x + n
        else:
            if -x % n == 0:
                answer = 0
            else:
                answer = x + n * (-x // n + 1)
    else:  # x > 0
        answer = x % n
    return answer


def move():
    global arr
    temp = [[deque() for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                while arr[i][j]:
                    m, s, d = arr[i][j].popleft()
                    nr, nc = i + dir[d][0] * s, j + dir[d][1] * s

                    # temp[calculate_pos(nr)][calculate_pos(nc)].append([m, s, d])
                    temp[(n + nr) % n][(n + nc) % n].append([m, s, d])

    arr = temp


def check():
    global arr
    temp = [[deque() for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if len(arr[i][j]) >= 2:
                length = len(arr[i][j])
                sum_m, sum_s = 0, 0
                flag_even = 0
                flag_odd = 0
                while arr[i][j]:
                    m, s, d = arr[i][j].popleft()
                    sum_m += m
                    sum_s += s
                    if d % 2 == 1:
                        flag_odd += 1
                    else:
                        flag_even += 1
                m = sum_m // 5
                s = sum_s // length
                if flag_even == length or flag_odd == length:
                    d = [0, 2, 4, 6]
                else:
                    d = [1, 3, 5, 7]
                if m != 0:
                    for k in range(4):
                        temp[i][j].append([m, s, d[k]])
            elif len(arr[i][j]) == 1:
                temp[i][j] = deepcopy(arr[i][j])
    arr = temp


ans = 0


def get_m():
    global ans
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                while arr[i][j]:

                    m, d, s = arr[i][j].popleft()

                    ans += m


# for i in range(n):
#     print(arr[i])
for i in range(k):
    move()
    # print("=============")
    # for i in range(n):
    #     print(arr[i])
    # print("=============")
    check()
    # print("=============")
    # for i in range(n):
    #     print(arr[i])
    # print("=============")

get_m()
print(ans)
