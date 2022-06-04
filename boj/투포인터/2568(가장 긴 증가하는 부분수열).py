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

line = []
for i in range(N):
    line.append(list(map(int, input().split())))

line = sorted(line, key=lambda x: x[1])


stack = [line[0][0]]

dp = [0] * N

for i in range(N):
    n = line[i][0]
    minBiggerIndex = bisect.bisect_left(stack, n)

    if stack[-1] < n:
        stack.append(n)
    else:
        stack[minBiggerIndex] = n

    dp[i] = minBiggerIndex

print(N - len(stack))


stack_len = len(stack)
ans = []
for i in range(N - 1, -1, -1):
    if dp[i] == stack_len - 1:
        ans.append(line[i][0])
        stack_len -= 1

dic = {}

for i in range(N):
    dic[line[i][0]] = 1

for i in ans:
    dic[i] -= 1
    if dic[i] == 0:
        del dic[i]

dic = sorted(dic)
for d in dic:
    print(d)
