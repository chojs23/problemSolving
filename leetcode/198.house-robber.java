import java.util.Arrays;

/*
 * @lc app=leetcode id=198 lang=java
 *
 * [198] House Robber
 */

// @lc code=start
class Solution {
    public int rob(int[] nums) {
        // dp[i]=max(dp[i-1],dp[i-2]+nums[i]);
        if (nums.length < 2) {
            return nums[0];
        }
        int[] dp = new int[nums.length];
        dp[0] = nums[0];
        dp[1] = Math.max(dp[0], nums[1]);

        for (int i = 2; i < nums.length; ++i) {

            dp[i] = Math.max(dp[i - 1], dp[i - 2] + nums[i]);

        }
        System.out.println(Arrays.toString(dp));

        return dp[nums.length - 1];
    }
}
// @lc code=end
