import sys
import bisect

input = sys.stdin.readline


N = int(input())
nums = list(map(int, input().split()))

stack = [nums[0]]


# stack에서의 인덱스를 저장
dp = [0] * N

# 기본 LIS
for i in range(N):
    n = nums[i]
    minBiggerIndex = bisect.bisect_left(stack, n)

    if stack[-1] < n:
        stack.append(n)
    else:
        stack[minBiggerIndex] = n

    dp[i] = minBiggerIndex

print(len(stack))


# DP의 특정 값에서 가장 마지막에 있는 원소가 정답이다.
# 가장 마지막으로 Replace했다는 것을 의미하기 때문이다.
# 이것을 (stack의 마지막 인덱스 ~ 0)까지 진행하면 된다.
toPrint = []
stack_len = len(stack)
for i in range(N - 1, -1, -1):
    if dp[i] == stack_len - 1:
        toPrint.append(nums[i])
        stack_len -= 1
print(*reversed(toPrint))
