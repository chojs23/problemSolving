#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        stack = []
        res = []

        def dfs(open, close):
            if open == close == n:
                res.append("".join(stack))

            if open < n:
                stack.append("(")
                dfs(open + 1, close)
                stack.pop()
            if close < open:
                stack.append(")")
                dfs(open, close + 1)
                stack.pop()

        dfs(0, 0)
        return res


# @lc code=end
