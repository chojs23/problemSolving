from copy import copy, deepcopy
import sys
from collections import defaultdict, deque
from itertools import permutations
import heapq

dr, dc = [-1, 1, 0, 0], [0, 0, 1, -1]

input = sys.stdin.readline
INF = sys.maxsize

# ===========================================================
sys.setrecursionlimit(10**8)
s = input().rstrip()
L = len(s)


dp = [2500 for _ in range(L + 1)]
dp[-1] = 0
is_p = [[0 for j in range(L)] for i in range(L)]


for i in range(L):  # 길이 1 짜리 팰린드롬
    is_p[i][i] = 1

for i in range(1, L):  # 길이 2 짜리 팰린드롬 (AA, DD 같은 놈들)
    if s[i - 1] == s[i]:
        is_p[i - 1][i] = 1

for l in range(3, L + 1):  # 길이 3 ~ L 짜리 팰린드롬
    for start in range(L - l + 1):
        end = start + l - 1
        if s[start] == s[end] and is_p[start + 1][end - 1]:
            # 처음과 끝이 같고, 그 사이가 팰린드롬이면
            is_p[start][end] = 1  # start~end 도 팰린드롬

for end in range(L):
    for start in range(end + 1):
        if is_p[start][end]:
            dp[end] = min(dp[end], dp[start - 1] + 1)
        else:
            dp[end] = min(dp[end], dp[end - 1] + 1)

print(dp[L - 1])
