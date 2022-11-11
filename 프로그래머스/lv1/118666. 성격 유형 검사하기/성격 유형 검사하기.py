import collections
import itertools
from copy import copy, deepcopy
from math import sqrt
import sys
from collections import defaultdict, deque
from itertools import combinations, permutations
import heapq
import bisect
import math

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

input = sys.stdin.readline
INF = sys.maxsize

# ==========================================================

q1, q2, q3, q4 = ["R", "T"], ["C", "F"], ["J", "M"], ["A", "N"]


def solution(survey, choices):
    answer = ""

    dic = {("R", "T"): [0, 0], ("C", "F"): [0, 0], ("J", "M"): [0, 0], ("A", "N"): [0, 0]}

    def makeChoice(s, choice):
        a, b = s
        pointA = 0
        pointB = 0

        if choice == 1:
            pointA += 3
        elif choice == 2:
            pointA += 2
        elif choice == 3:
            pointA += 1
        elif choice == 4:
            pass
        elif choice == 5:
            pointB += 1
        elif choice == 6:
            pointB += 2
        else:
            pointB += 3

        if (a, b) in dic.keys():
            dic[(a, b)][0] += pointA
            dic[(a, b)][1] += pointB
        if (b, a) in dic.keys():
            dic[(b, a)][1] += pointA
            dic[(b, a)][0] += pointB

    for i, s in enumerate(survey):
        a, b = s

        makeChoice(s, choices[i])


    for d in dic:
        a, b = d

        if dic[(a, b)][0] < dic[(a, b)][1]:
            answer += b
        else:
            answer += a
    return answer

