package 프로그래머스.lv1;

import java.util.*;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        int n = board.length;
        Stack<Integer> box = new Stack<>();
        for (int m : moves) {
            m -= 1;
            for (int i = 0; i < n; i++) {
                if (board[i][m] != 0) {

                    box.push(board[i][m]);
                    board[i][m] = 0;
                    break;
                }
            }
            if (box.size() > 1 && box.get(box.size() - 2) == box.peek()) {
                answer += 2;

                box.pop();
                box.pop();
            }
        }

        return answer;
    }
}