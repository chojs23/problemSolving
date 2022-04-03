/*
 * @lc app=leetcode id=169 lang=java
 *
 * [169] Majority Element
 */

// @lc code=start
class Solution {
    public int majorityElement(int[] nums) {

        int candidate = nums[0], count = 0;

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == candidate) {
                count += 1;
            } else
                count -= 1;
            if (count == 0) {
                candidate = nums[i];
                count = 1;
            }
        }
        return candidate;
    }
}
// @lc code=end
