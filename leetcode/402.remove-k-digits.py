#
# @lc app=leetcode id=402 lang=python3
#
# [402] Remove K Digits
#

# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        # 1 2 3 4 5 6 7 8 0
        for n in num:
            while k > 0 and stack and stack[-1] > n:
                k -= 1
                stack.pop()
            stack.append(n)
        stack = stack[: len(stack) - k]
        return str(int("".join(stack))) if stack else "0"


# @lc code=end
