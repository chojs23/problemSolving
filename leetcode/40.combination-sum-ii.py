#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        cur = []
        result = []
        candidates.sort()
        n = len(candidates)

        def dfs(start, target):
            if target == 0:
                result.append(cur[:])
            if target <= 0:
                return

            prev = -1
            for i in range(start, n):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                dfs(i + 1, target - candidates[i])
                cur.pop()
                prev = candidates[i]

        dfs(0, target)

        return result


# @lc code=end
