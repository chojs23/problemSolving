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


N,M=map(int,input().split())

switch=defaultdict(list)

for _ in range(M):
    x,y,a,b=map(int,input().split())
    switch[(x-1,y-1)].append((a-1,b-1))

room=[[0]*N for _ in range(N)]
room[0][0]=1

def bfs():
    q=deque()
    q.append([0,0])
    visited=[[0]*N for _ in range(N)]
    visited[0][0]=1
    res=1
    while q:
        r,c=q.popleft()
        
        for s in switch[(r,c)]:
            a,b=s
            if room[a][b]==0:
                res+=1
                room[a][b]=1

                for i in range(4):
                    nr,nc=a+dr[i],b+dc[i]
                    if 0<=nr<N and 0<=nc<N and visited[nr][nc]:
                        q.append([nr,nc])

        for i in range(4):
            nr,nc=r+dr[i],c+dc[i]

            if 0<=nr<N and 0<=nc<N and not visited[nr][nc] and room[nr][nc]==1:
                q.append([nr,nc])
                visited[nr][nc]=1

    return res


res=bfs()

print(res)