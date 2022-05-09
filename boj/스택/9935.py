from copy import copy, deepcopy
import sys
from collections import deque
from itertools import permutations
import heapq

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

input = sys.stdin.readline

# ===========================================================


string = input().rstrip()

bomb = input().rstrip()


lastChar = bomb[-1]
stack = []
length = len(bomb)

for s in string:
    stack.append(s)

    if s == lastChar and "".join(stack[-length:]) == bomb:

        for _ in range(length):
            stack.pop()

answer = "".join(stack)

print(answer) if answer != "" else print("FRULA")
