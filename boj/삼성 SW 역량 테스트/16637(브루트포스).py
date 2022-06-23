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


N = int(input())

s = input()

nums, op = [], []
for i in range(N):
    if i % 2 == 0:
        nums.append(s[i])
    else:
        op.append(s[i])

ans = -INF


def dfs(idx, sub_total):
    global ans

    if idx == len(op):
        ans = max(ans, int(sub_total))
        return

    # (3 + 8) * 7 - 9 * 2 부터 시작.
    first = str(eval(sub_total + op[idx] + nums[idx + 1]))
    dfs(idx + 1, first)

    if idx + 1 < len(op):
        # 3 + (8 * 7) - 9 * 2 부터 시작
        second = str(eval(nums[idx + 1] + op[idx + 1] + nums[idx + 2]))
        second = str(eval(sub_total + op[idx] + second))
        # op를 2개 소모했으므로 idx + 2
        dfs(idx + 2, second)


dfs(0, nums[0])
print(ans)
