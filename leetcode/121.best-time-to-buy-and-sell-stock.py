#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        buy = 10 ** 4 + 1
        for price in prices:
            if buy > price:
                buy = price
            ans = max(ans, price - buy)
        return ans


# @lc code=end
