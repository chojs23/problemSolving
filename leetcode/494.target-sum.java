import java.util.HashMap;
import java.util.Map;

/*
 * @lc app=leetcode id=494 lang=java
 *
 * [494] Target Sum
 */

// @lc code=start
class Solution {
    Map<String, Integer> dp = new HashMap<>();
    int[] nums;
    int target;

    public int findTargetSumWays(int[] nums, int target) {
        this.nums = nums;
        this.target = target;
        int ans = dfs(0, 0);
        // System.out.println(dp);
        return ans;
    }

    public int dfs(int i, int total) {
        if (i == nums.length) {
            return (total == target) ? 1 : 0;
        }
        String key = i + "()" + total;

        if (dp.containsKey(key)) {
            return dp.get(key);
        }

        dp.put(key, dfs(i + 1, total + nums[i]) + dfs(i + 1, total - nums[i]));
        return dp.get(key);
    }
}
// @lc code=end
