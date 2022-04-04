import java.util.ArrayList;
import java.util.List;

/*
 * @lc app=leetcode id=77 lang=java
 *
 * [77] Combinations
 */

// @lc code=start
class Solution {
    List<List<Integer>> res = new ArrayList<>();

    ArrayList<Integer> temp = new ArrayList<>();

    public List<List<Integer>> combine(int n, int k) {

        dfs(1, n, k);
        return res;

    }

    public void dfs(int start, int n, int k) {
        if (temp.size() == k) {
            res.add(new ArrayList<>(temp));
        }

        for (int i = start; i < n + 1; i++) {
            temp.add(i);
            dfs(i + 1, n, k);
            temp.remove(temp.size() - 1);
        }

    }
}
// @lc code=end
