/*
 * @lc app=leetcode id=338 lang=java
 *
 * [338] Counting Bits
 */

// @lc code=start
class Solution {
    public int[] countBits(int n) {
        int[] answer = new int[n + 1];

        if (n >= 0)
            answer[0] = 0;

        for (int i = 1; i <= n; i++) {

            answer[i] = answer[i / 2] + i % 2;

        }

        return answer;
    }
}
// @lc code=end
