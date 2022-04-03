
/*
 * @lc app=leetcode id=79 lang=java
 *
 * [79] Word Search
 */

// @lc code=start
class Solution {
    public boolean exist(char[][] board, String word) {
        int r = board.length;
        int c = board[0].length;

        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (dfs(board, word, i, j, 0)) {
                    return true;
                }
            }
        }
        return false;
    }

    private static final int[][] DIRS = new int[][] {
            { 1, 0 }, { -1, 0 }, { 0, 1 }, { 0, -1 } };

    private boolean dfs(char[][] board, String word, int r, int c, int i) {
        if (i == word.length()) {
            return true;
        }
        if (r < 0 || c < 0 || r >= board.length
                || c >= board[0].length
                || word.charAt(i) != board[r][c]
                || board[r][c] == '#') {
            return false;
        }

        char temp = board[r][c];
        board[r][c] = '#';
        boolean res = false;
        for (var dir : DIRS) {
            if (dfs(board, word, r + dir[0], c + dir[1], i + 1)) {
                res = true;
            }
        }
        board[r][c] = temp;
        return res;
    }
}
// @lc code=end
