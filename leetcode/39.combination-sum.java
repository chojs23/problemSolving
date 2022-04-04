import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/*
 * @lc app=leetcode id=39 lang=java
 *
 * [39] Combination Sum
 */

// @lc code=start
class Solution {
    List<List<Integer>> res = new ArrayList<>();
    List<Integer> temp = new ArrayList<>();
    int target;
    int[] candidates;

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        this.target = target;
        this.candidates = candidates;
        dfs(0);
        return res;
    }

    public void dfs(int start) {
        if (temp.stream().mapToInt(i -> i).sum() > target) {
            return;
        }

        if (temp.stream().mapToInt(i -> i).sum() == target) {
            res.add(new ArrayList<>(temp));
            return;
        }

        for (int i = start; i < candidates.length; i++) {
            temp.add(candidates[i]);
            dfs(i);
            temp.remove(temp.size() - 1);
        }

    }
}
// @lc code=end
