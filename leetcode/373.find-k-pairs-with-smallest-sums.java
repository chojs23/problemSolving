import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Set;

/*
 * @lc app=leetcode id=373 lang=java
 *
 * [373] Find K Pairs with Smallest Sums
 */

// @lc code=start
class Solution {
    public List<List<Integer>> kSmallestPairs(int[] nums1, int[] nums2, int k) {
        PriorityQueue<Tuple> q = new PriorityQueue<>((a, b) -> a.val - b.val);
        List<List<Integer>> res = new ArrayList<>();
        Set<String> visited = new HashSet<>();
        if (nums1 == null || nums1.length == 0 || nums2 == null || nums2.length == 0 || k <= 0)
            return res;

        q.offer(new Tuple(0, 0, nums1[0] + nums2[0]));

        visited.add(new String("0,0"));

        while (res.size() < k & !q.isEmpty()) {
            Tuple cur = q.poll();
            res.add(Arrays.asList(nums1[cur.x], nums2[cur.y]));

            if (cur.x + 1 < nums1.length & !visited.contains(String.format("%d,%d", cur.x + 1, cur.y))) {
                q.offer(new Tuple(cur.x + 1, cur.y, nums1[cur.x + 1] + nums2[cur.y]));
                visited.add(String.format("%d,%d", cur.x + 1, cur.y));
            }
            if (cur.y + 1 < nums2.length & !visited.contains(String.format("%d,%d", cur.x, cur.y + 1))) {
                q.offer(new Tuple(cur.x, cur.y + 1, nums1[cur.x] + nums2[cur.y + 1]));
                visited.add(String.format("%d,%d", cur.x, cur.y + 1));
            }

        }

        return res;
    }

    class Tuple implements Comparable<Tuple> {
        int x, y, val;

        public Tuple(int x, int y, int val) {
            this.x = x;
            this.y = y;
            this.val = val;
        }

        @Override
        public int compareTo(Solution.Tuple o) {
            // TODO Auto-generated method stub
            return 0;
        }

        @Override
        public String toString() {
            return String.format("(%d,%d,%d)", x, y, val);
        }

    }
}
// @lc code=end
