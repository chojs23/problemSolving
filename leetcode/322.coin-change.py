# @before-stub-for-debug-begin
from cmath import inf
from python3problem322 import *
from typing import *

# @before-stub-for-debug-end

#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [inf] * (amount + 1)
        # dp[i]=min(for dp[i-coin]+1)

        for coin in coins:
            if coin <= amount:
                dp[coin] = 1
        dp[0] = 0
        for i in range(1, amount + 1):
            if dp[i] == inf:
                dp[i] = min(dp[i - coin] if i - coin > 0 else inf for coin in coins) + 1

        return dp[amount] if dp[amount] != inf else -1


# @lc code=end
