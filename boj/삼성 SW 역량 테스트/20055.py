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

n, k = map(int, input().split())

a = list(map(int, input().split()))

belt = [i for i in range(2 * n)]


def rotate(belt):
    n = len(belt) / 2
    next1 = belt[0]
    for i in range(int(2 * n)):
        next2 = belt[(i + 1) % int(2 * n)]
        belt[(i + 1) % int(2 * n)] = next1
        next1 = next2
    # print(belt)


ans = 0
robot = [0] * (n)

while True:
    ans += 1
    # a.insert(0, a[-1])
    # a = a[: (len(a) - 1)]

    # robot.insert(0, robot[-1])
    # robot = robot[: (len(robot) - 1)]
    rotate(belt)
    rotate(robot)

    if robot[-1] != 0:
        robot[-1] = 0

    for i in range(n - 2, -1, -1):
        # print(i)
        if robot[i] != 0:
            if robot[i + 1] == 0 and a[belt[i + 1]] > 0:
                robot[i + 1] = 1
                robot[i] = 0
                a[belt[i + 1]] -= 1

    if robot[-1] != 0:
        robot[-1] = 0

    if a[belt[0]] > 0:
        robot[0] = 1
        a[belt[0]] -= 1

    cnt = 0

    if a.count(0) >= k:
        break


print(ans)
