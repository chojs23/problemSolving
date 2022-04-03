import java.util.HashMap;
import java.util.Map;

/*
 * @lc app=leetcode id=287 lang=java
 *
 * [287] Find the Duplicate Number
 */

// @lc code=start
class Solution {
    public int findDuplicate(int[] nums) {
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();

        for (int n : nums) {
            map.put(n, map.getOrDefault(n, 0) + 1);
            if (map.get(n) == 2) {
                return n;
            }
        }
        System.out.println(map.toString());

        return 0;
    }
}
// @lc code=end
