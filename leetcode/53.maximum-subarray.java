import java.util.Arrays;

/*
 * @lc app=leetcode id=53 lang=java
 *
 * [53] Maximum Subarray
 */

// @lc code=start
class Solution {
    public int maxSubArray(int[] nums) {
        int[] dp = new int[nums.length];

        int idx = 0;
        for (int n : nums) {
            dp[idx] = n;
            idx += 1;
        }
        int max = dp[0];
        for (int i = 1; i < nums.length; i++) {
            dp[i] = nums[i] + (dp[i - 1] > 0 ? dp[i - 1] : 0);
            max = Math.max(dp[i], max);

        }

        System.out.println(Arrays.toString(dp));

        return max;
    }
}
// @lc code=end
