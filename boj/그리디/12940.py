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

S = input().rstrip()
T = input().rstrip()

"""

해당 문제가 그리디인 이유는, 사실상 두 가지라고 생각했던 선택지가 단 한 가지이기 때문입니다.

발상을 바꾸어 봅시다. 기존의 S -> T로 뻗어나가는 방식 말고, 반대로 T에서 출발해 S가 나올 수 있는지를 한 번 확인해 봅시다.

preview
이런 식으로 가능한 경우를 뻗어 나가겠지요...

그런데 조금 더 생각해 보면, 사실 어떻게 뻗어지는지는 이미 정해져 있습니다. 한 번 예를 들어 봅시다.

1) 문자열 T의 마지막 문자가 A일 경우

문자열의 뒤에 A를 추가한다.
문자열을 뒤집고 뒤에 B를 추가한다. 이 경우는 불가능하게 됩니다. 왜냐하면 2번 연산을 했을 경우 마지막 문자는 B여야 하기 때문입니다.
2) 문자열 T의 마지막 문자가 B일 경우

문자열의 뒤에 A를 추가한다. 이 경우는 불가능하게 됩니다. 왜냐하면 1번 연산을 했을 경우 마지막 문자는 A여야 하기 때문입니다.
문자열을 뒤집고 뒤에 B를 추가한다.
즉 문자열 T의 마지막 문자가 A라면 그 직전의 연산은 반드시 1번 연산, 마지막 문자가 B라면 그 직전의 연산은 반드시 2번 연산이었어야 모순되지 않는다는 것입니다. 그렇기 때문에, 실제로 우리가 생각했던 가지는...

preview
이렇게 되는 겁니다. 그야말로... 답정너가 아닐 수가 없습니다.

가지를 뻗어나갔을 때의 형태는 위의 그림과 같게 되며, 마지막 문자가 주어졌을 경우 그 상태에서 할 수 있는 연산의 종류는 1종류이니, 그 연산을 반복하면서 문자열 T에서 S로 거꾸로 뻗어나가는 과정을 거치면 됩니다. 그 결과 문자열 S가 나오게 되면 가능한 경우고, 문자열이 한 글자가 되어 더 이상 연산을 할 수 없는 상황이 되면 불가능한 경우라고 결론지을 수 있게 됩니다.

예제 1번을 위의 논리대로 적용하면 이렇게 됩니다:

"""


def sol(s):
    # print(s)
    if s == S:
        print(1)
        exit()
    if len(s) <= len(S):
        return
    if s[-1] == "A":
        sol(s[:-1])
    if s[-1] == "B":
        temp = s[:-1]
        temp = temp[::-1]
        sol(temp)


sol(T)
print(0)
