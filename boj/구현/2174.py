import collections
import itertools
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

A, B = map(int, input().split())
N, M = map(int, input().split())

brd = [[0] * A for _ in range(B)]

NESW_dic = {
    'N': 0,
    'E': 1,
    'S': 2,
    'W': 3,
}

NESW_list = [
    [-1, 0],
    [0, 1],
    [1, 0],
    [0, -1]
]

# 로봇 위치 및 방향 정보 받기
robots = []
for i in range(N):
    x, y, d = input().split()
    r, c = B - int(y), int(x) - 1
    robots.append([r, c, NESW_dic[d]])
    brd[r][c] = i+1

# 명령 실행
flag = False
for i in range(M):
    robot, instruction, loop = input().split()
    robot = int(robot)
    loop = int(loop)

    r, c, d = robots[robot-1]
    if instruction == 'L' or instruction == 'R':
        new_d = (d + loop) % 4
        if loop % 2:
            if instruction == 'L':
                new_d = (new_d + 2) % 4
        robots[robot-1] = [r, c, new_d]
    else:
        dr, dc = NESW_list[d]
        for j in range(1, loop+1):

            if 0 <= r + dr < B and 0 <= c + dc < A:
                if brd[r+dr][c+dc]:
                    flag = True
                    print(
                        f'Robot {brd[r][c]} crashes into robot {brd[r + dr][c + dc]}')
                    break
                else:
                    brd[r][c] = 0
                    r, c = r + dr, c + dc
                    brd[r][c] = robot
                    robots[robot-1] = [r, c, d]
            else:
                flag = True
                print(f'Robot {brd[r][c]} crashes into the wall')
                break
    if flag:
        break

if not flag:
    print('OK')
