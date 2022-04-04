import java.util.Arrays;

/*
 * @lc app=leetcode id=322 lang=java
 *
 * [322] Coin Change
 */

// @lc code=start
class Solution {
    public int coinChange(int[] coins, int amount) {
        if (coins == null || coins.length == 0 || amount <= 0)
            return 0;
        int[] minNumber = new int[amount + 1];
        for (int i = 1; i <= amount; i++) {
            minNumber[i] = Integer.MAX_VALUE;
            for (int j = 0; j < coins.length; j++) {
                if (coins[j] <= i && minNumber[i - coins[j]] != Integer.MAX_VALUE)
                    minNumber[i] = Integer.min(minNumber[i], 1 + minNumber[i - coins[j]]);
            }
        }
        if (minNumber[amount] == Integer.MAX_VALUE)
            return -1;
        else
            return minNumber[amount];

    }
}
// @lc code=end
