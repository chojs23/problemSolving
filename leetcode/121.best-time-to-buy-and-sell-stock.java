/*
 * @lc app=leetcode id=121 lang=java
 *
 * [121] Best Time to Buy and Sell Stock
 */

// @lc code=start
class Solution {
    public int maxProfit(int[] prices) {
        int min = (int) Math.pow(10, 4);
        int max = 0;
        for (int p : prices) {
            if (p < min) {
                min = p;
                continue;
            }
            max = Math.max(max, p - min);

        }

        return max;

    }
}
// @lc code=end
