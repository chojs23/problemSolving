import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/*
 * @lc app=leetcode id=22 lang=java
 *
 * [22] Generate Parentheses
 */

// @lc code=start
class Solution {
    List<String> res = new ArrayList<>();
    List<String> temp = new ArrayList<>();
    int n;

    public List<String> generateParenthesis(int n) {
        this.n = n;
        dfs(0, 0);
        return res;
    }

    public void dfs(int open, int close) {
        if (open == close && close == n) {
            res.add(String.join("", temp));
        }
        if (open < n) {
            temp.add("(");
            dfs(open + 1, close);
            temp.remove(temp.size() - 1);
        }
        if (close < open) {
            temp.add(")");
            dfs(open, close + 1);
            temp.remove(temp.size() - 1);
        }

    }
}
// @lc code=end
