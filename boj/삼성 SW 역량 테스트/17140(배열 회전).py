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

r, c, k = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(3)]


ans = 0
flag = 1
while ans <= 100:
    try:
        if a[r - 1][c - 1] == k:
            print(ans)
            flag = 0
            break
    except:
        pass

    rlen, clen = len(a), len(a[0])

    dic = {}

    # R
    if rlen >= clen:
        max_len = 0
        for i in range(rlen):
            dic = {}

            for j in range(clen):
                if a[i][j] == 0:
                    continue
                if a[i][j] in dic:
                    dic[a[i][j]] += 1
                else:
                    dic[a[i][j]] = 1
            dic_sorted = sorted(dic.items(), key=lambda x: (x[1], x[0]))

            new_list = []
            for q in range(len(dic)):
                new_list.append(dic_sorted[q][0])
                new_list.append(dic_sorted[q][1])
            if len(new_list) > 100:
                new_list = new_list[:100]
            max_len = max(max_len, len(new_list))

            a[i] = copy(new_list)

        for idx in range(rlen):
            if len(a[idx]) < max_len:
                for _ in range(max_len - len(a[idx])):
                    a[idx].append(0)

    # C
    else:
        max_len = 0
        a = list(zip(*a))
        rlen, clen = len(a), len(a[0])
        for i in range(rlen):
            dic = {}

            for j in range(clen):
                if a[i][j] == 0:
                    continue
                if a[i][j] in dic:
                    dic[a[i][j]] += 1
                else:
                    dic[a[i][j]] = 1
            dic_sorted = sorted(dic.items(), key=lambda x: (x[1], x[0]))

            new_list = []
            for q in range(len(dic)):
                new_list.append(dic_sorted[q][0])
                new_list.append(dic_sorted[q][1])
            if len(new_list) > 100:
                new_list = new_list[:100]
            max_len = max(max_len, len(new_list))

            a[i] = copy(new_list)

        for idx in range(rlen):
            if len(a[idx]) < max_len:
                for _ in range(max_len - len(a[idx])):
                    a[idx].append(0)
        a = list(zip(*a))

    ans += 1

if flag:
    print(-1)
