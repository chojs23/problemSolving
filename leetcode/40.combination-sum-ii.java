import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/*
 * @lc app=leetcode id=40 lang=java
 *
 * [40] Combination Sum II
 */

// @lc code=start
class Solution {
    List<List<Integer>> res = new ArrayList<>();
    List<Integer> temp = new ArrayList<>();
    int target;
    int[] candidates;

    public List<List<Integer>> combinationSum2(int[] candidates, int target) {

        this.target = target;
        Arrays.sort(candidates);
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
        int prev = -1;
        for (int i = start; i < candidates.length; i++) {
            if (candidates[i] == prev) {
                continue;
            }
            prev = candidates[i];
            temp.add(candidates[i]);
            dfs(i + 1);
            temp.remove(temp.size() - 1);
        }
    }
}
// @lc code=end
