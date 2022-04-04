import java.util.ArrayList;
import java.util.List;

/*
 * @lc app=leetcode id=216 lang=java
 *
 * [216] Combination Sum III
 */

// @lc code=start
class Solution {
    List<List<Integer>> res = new ArrayList<>();
    List<Integer> temp = new ArrayList<>();
    int k;
    int n;

    public List<List<Integer>> combinationSum3(int k, int n) {
        this.k = k;
        this.n = n;
        dfs(1, 0);
        return res;
    }

    public void dfs(int start, int idx) {
        if (idx == k & temp.stream().mapToInt(i -> i).sum() == n) {
            res.add(new ArrayList<>(temp));
            return;
        }
        if (temp.stream().mapToInt(i -> i).sum() > n | idx > k) {
            return;
        }

        for (int i = start; i < 10; i++) {
            if (temp.stream().mapToInt(j -> j).sum() + i > n) {
                continue;
            }
            temp.add(i);
            dfs(i + 1, idx + 1);
            temp.remove(temp.size() - 1);
        }

    }
}
// @lc code=end
