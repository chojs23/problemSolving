import java.util.ArrayList;
import java.util.List;

/*
 * @lc app=leetcode id=784 lang=java
 *
 * [784] Letter Case Permutation
 */

// @lc code=start
class Solution {
    public List<String> letterCasePermutation(String s) {
        List<String> res = new ArrayList<>();
        dfs(res, 0, s.toCharArray());
        return res;
    }

    public void dfs(List<String> res, int i, char[] s) {
        if (i == s.length) {
            res.add(new String(s));
        } else {
            if (Character.isLetter(s[i])) {
                s[i] = Character.toUpperCase(s[i]);
                dfs(res, i + 1, s);
                s[i] = Character.toLowerCase(s[i]);
                dfs(res, i + 1, s);
            } else {
                dfs(res, i + 1, s);
            }
        }
    }
}
// @lc code=end
