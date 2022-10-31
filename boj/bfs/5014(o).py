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

# ==========================================================

F,S,G,U,D=map(int,input().split())

btn=[U,-D]
def bfs():
    if S==G:
        return 0
    visited=[0]*(F+1)
    q=deque()
    q.append(S)
    cnt=0
    visited[S]=1
    while q:
        length=len(q)
        cnt+=1

        for i in range(length):
            cur=q.popleft()

            for j in range(2):
                ncur=cur+btn[j]

                if 0<ncur<=F and not visited[ncur]:
                    if ncur==G:
                        return cnt
                    visited[ncur]=1

                    q.append(ncur)

    return "use the stairs"


print(bfs())