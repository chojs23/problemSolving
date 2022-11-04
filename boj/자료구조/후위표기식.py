import sys
from collections import deque
from itertools import permutations
import heapq

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

input = sys.stdin.readline

# ===========================================================

exp = input().rstrip()

res = ""
stk = []

for s in exp:
    if s.isalpha():
        res += s
    else:
        if s == "(":
            stk.append(s)
        elif s == "*" or s == "/":
            while stk and (stk[-1] == "*" or stk[-1] == "/"):
                res += stk.pop()
            stk.append(s)
        elif s == "+" or s == "-":
            while stk and stk[-1] != "(":
                res += stk.pop()
            stk.append(s)
        else:
            while stk and stk[-1] != "(":
                res += stk.pop()
            stk.pop()

while stk:
    res += stk.pop()

print(res)
