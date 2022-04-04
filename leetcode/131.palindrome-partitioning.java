import java.util.ArrayList;
import java.util.List;

/*
 * @lc app=leetcode id=131 lang=java
 *
 * [131] Palindrome Partitioning
 */

// @lc code=start
class Solution {
    List<List<String>> res = new ArrayList<>();
    List<String> part = new ArrayList<>();
    String s;

    public List<List<String>> partition(String s) {
        this.s = s;
        dfs(0);
        return res;
    }

    public boolean isPalindrome(String s, int start, int end) { // A simple palindromic function start from 0 go till
                                                                // end. And basically keep on checking till they don't
                                                                // cross.
        while (start <= end) {
            if (s.charAt(start++) != s.charAt(end--))
                return false;
        }
        return true;
    }

    public void dfs(int i) {
        if (i >= s.length()) {
            res.add(new ArrayList<>(part));
        }
        for (int j = i; j < s.length(); j++) {
            if (isPalindrome(s, i, j)) {
                part.add(s.substring(i, j + 1));
                dfs(j + 1);
                part.remove(part.size() - 1);
            }
        }
    }
}
// @lc code=end
