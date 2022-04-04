#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        s = []
        result = []

        def dfs(start):
            if len(s) == k:
                result.append(s[:])

            for i in range(start, n + 1):
                # if i not in s:
                #     if len(s) >= 1:
                #         if i > s[-1]:
                #             s.append(i)
                #             dfs(i + 1)
                #             s.pop()
                #     else:
                s.append(i)
                dfs(i + 1)
                s.pop()

        dfs(1)
        return result


# @lc code=end
