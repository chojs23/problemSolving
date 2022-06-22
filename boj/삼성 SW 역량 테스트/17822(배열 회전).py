from copy import copy, deepcopy
from math import sqrt
import sys
from collections import defaultdict, deque
from itertools import permutations
import heapq
import bisect

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

input = sys.stdin.readline
INF = sys.maxsize

# ===========================================================

n, m, t = map(int, input().split())
circle = []
rotation = []
for i in range(n):
    nums = list(map(int, input().split()))
    circle.append(nums)

for i in range(t):
    rotation.append(list(map(int, input().split())))


def check(erase):
    for i in range(n):
        for j in range(m):
            if circle[i][j] == 0:
                continue
            if j == 0:
                if i < n - 1:
                    if circle[i][j] == circle[i][j + 1]:
                        erase.add((i, j))
                        erase.add((i, j + 1))
                    if circle[i][j] == circle[i][m - 1]:
                        erase.add((i, j))
                        erase.add((i, m - 1))
                    if circle[i][j] == circle[i + 1][j]:
                        erase.add((i, j))
                        erase.add((i + 1, j))
                else:
                    if circle[i][j] == circle[i][j + 1]:
                        erase.add((i, j))
                        erase.add((i, j + 1))
                    if circle[i][j] == circle[i][m - 1]:
                        erase.add((i, j))
                        erase.add((i, m - 1))

            if 1 <= j < m - 1:
                if i < n - 1:
                    if circle[i][j] == circle[i][j + 1]:
                        erase.add((i, j))
                        erase.add((i, j + 1))
                    if circle[i][j] == circle[i][j - 1]:
                        erase.add((i, j))
                        erase.add((i, j - 1))
                    if circle[i][j] == circle[i + 1][j]:
                        erase.add((i, j))
                        erase.add((i + 1, j))
                else:
                    if circle[i][j] == circle[i][j + 1]:
                        erase.add((i, j))
                        erase.add((i, j + 1))
                    if circle[i][j] == circle[i][j - 1]:
                        erase.add((i, j))
                        erase.add((i, j - 1))
            if j == m - 1:
                if i < n - 1:
                    if circle[i][j] == circle[i][0]:
                        erase.add((i, j))
                        erase.add((i, 0))
                    if circle[i][j] == circle[i][j - 1]:
                        erase.add((i, j))
                        erase.add((i, j - 1))
                    if circle[i][j] == circle[i + 1][j]:
                        erase.add((i, j))
                        erase.add((i + 1, j))
                else:
                    if circle[i][j] == circle[i][0]:
                        erase.add((i, j))
                        erase.add((i, 0))
                    if circle[i][j] == circle[i][j - 1]:
                        erase.add((i, j))
                        erase.add((i, j - 1))
    return erase


# m= 0 1 2 3 k=2 0-2 1-3 2-0 3-1   i+k%m m=4
# m= 0 1 2 3 4 k=2 0-3 1-4 2-0 3-1 4-2  m+i-k%m m=5
def rotate(idx, d, k):
    for _ in range(k):
        if d == 0:
            temp1 = circle[idx][0]
            for i in range(m - 1):
                temp2 = circle[idx][i + 1]
                circle[idx][i + 1] = temp1
                temp1 = temp2
            circle[idx][0] = temp2

        else:
            temp1 = circle[idx][0]
            for i in range(m - 1):
                temp2 = circle[idx][m - (i + 1)]
                circle[idx][m - (i + 1)] = temp1
                temp1 = temp2
            circle[idx][0] = temp2


for i in rotation:
    x, d, k = i

    for j in range(n):
        if (j + 1) % x == 0:
            # print("rotate", j, d, k)
            rotate(j, d, k)

        else:
            continue
    # print(circle)
    erase = set()
    res = check(erase)
    # print(res)
    if res:
        for e in res:
            r, c = e
            circle[r][c] = 0
    else:
        s = 0
        cnt = 0
        for i in range(n):
            for j in range(m):
                if circle[i][j] != 0:
                    cnt += 1
                    s += circle[i][j]
        if cnt != 0:
            avg = s / cnt
        for i in range(n):
            for j in range(m):
                if circle[i][j] == 0:
                    continue
                else:
                    if circle[i][j] > avg:
                        circle[i][j] -= 1
                    elif circle[i][j] < avg:
                        circle[i][j] += 1

    ans = 0
    for i in circle:
        ans += sum(i)


print(ans)
