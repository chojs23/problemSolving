#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change 2
#

# @lc code=start
class Solution:
    def change(self, n: int, money: List[int]) -> int:

        dp = [[0] * (len(money) + 1) for _ in range(n + 1)]
        dp[0] = [1] * (len(money) + 1)

        for a in range(1, n + 1):
            for i in range(len(money) - 1, -1, -1):
                dp[a][i] = dp[a][i + 1]
                if a - money[i] >= 0:
                    dp[a][i] += dp[a - money[i]][i]
        return dp[n][0]


# @lc code=end
