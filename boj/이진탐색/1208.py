from copy import copy, deepcopy
import sys
from collections import defaultdict, deque
from itertools import permutations
import heapq

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

input = sys.stdin.readline

# ===========================================================

N, S = map(int, input().split())

nums = list(map(int, input().rstrip().split()))


left, right = nums[: N // 2], nums[N // 2 :]
left_sum, right_sum = [0], [0]


def l_dfs(idx, sum):
    if idx > len(left) - 1:
        return
    sum += left[idx]
    left_sum.append(sum)
    l_dfs(idx + 1, sum)
    l_dfs(idx + 1, sum - left[idx])


def r_dfs(idx, sum):
    if idx > len(right) - 1:
        return
    sum += right[idx]
    right_sum.append(sum)
    r_dfs(idx + 1, sum)
    r_dfs(idx + 1, sum - right[idx])


l_dfs(0, 0)
r_dfs(0, 0)

left_sum.sort()
right_sum.sort()


left_pointer = 0
right_pointer = len(right_sum) - 1
ans = 0

while left_pointer < len(left_sum) and right_pointer >= 0:
    tmp = left_sum[left_pointer] + right_sum[right_pointer]

    # 두 포인터가 가르키는 값의 합이 s와 같다면
    if tmp == S:

        # 부분집합의 합이 같은 경우를 예외처리
        same_count_left = 1
        same_count_right = 1

        same_left_idx = left_pointer
        same_right_idx = right_pointer

        left_pointer += 1
        right_pointer -= 1

        while (
            left_pointer < len(left_sum)
            and left_sum[left_pointer] == left_sum[same_left_idx]
        ):
            same_count_left += 1
            left_pointer += 1

        while (
            right_pointer >= 0 and right_sum[right_pointer] == right_sum[same_right_idx]
        ):
            same_count_right += 1
            right_pointer -= 1

        ans += same_count_left * same_count_right

    elif tmp < S:
        left_pointer += 1

    else:
        right_pointer -= 1

# 아무것도 뽑지 않는 경우는 고려하지 않으므로, s가 0이라면 해당 경우의 수 1개를 빼준다
if S == 0:
    ans -= 1

print(ans)
