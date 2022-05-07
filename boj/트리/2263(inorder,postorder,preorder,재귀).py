from copy import copy, deepcopy
import sys
from collections import deque
from itertools import permutations
import heapq

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

input = sys.stdin.readline

# ===========================================================
sys.setrecursionlimit(10**9)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
position = [0] * (n + 1)


# inorder 구조
# left - root - right
# postorder 구조
# left - right - root

# post의 마지막노트는 트리의 루트임
# 그 루트로 left - root - right 나눠서 재귀로 돌림

# https://whereisend.tistory.com/112

for i in range(n):
    position[inorder[i]] = i


def preorder(instart, inend, poststart, postend):
    if instart > inend or poststart > postend:
        return

    root = postorder[postend]
    print(root, end=" ")

    left_cnt = position[root] - instart
    right_cnt = inend - position[root]

    preorder(instart, position[root] - 1, poststart, poststart + left_cnt - 1)
    preorder(position[root] + 1, inend, postend - right_cnt, postend - 1)


preorder(0, n - 1, 0, n - 1)
