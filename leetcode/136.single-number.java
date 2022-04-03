/*
 * @lc app=leetcode id=136 lang=java
 *
 * [136] Single Number
 */

// @lc code=start
class Solution {
    public int singleNumber(int[] nums) {
        int ans =0;
    
        int len = nums.length;
        for(int i=0;i!=len;i++)
            ans ^= nums[i];
        
        return ans;
    }
}
// @lc code=end

