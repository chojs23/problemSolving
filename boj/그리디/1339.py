import copy
from math import sqrt
import sys
from collections import defaultdict, deque
from itertools import permutations, combinations
import heapq
import bisect

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

input = sys.stdin.readline
INF = sys.maxsize

# ===========================================================

n = int(input())

word = [input().rstrip() for _ in range(n)]

dict = {}

for i in range(n):
    for j in range(len(word[i])):
        if word[i][j] in dict:
            dict[word[i][j]] += 10 ** (len(word[i]) - j - 1)
        else:
            dict[word[i][j]] = 10 ** (len(word[i]) - j - 1)

nums = []

for v in dict.values():
    nums.append(v)

nums.sort(reverse=True)

ans = 0
pows = 9
for i in nums:
    ans += pows * i
    pows -= 1
print(ans)
