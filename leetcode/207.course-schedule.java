import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/*
 * @lc app=leetcode id=207 lang=java
 *
 * [207] Course Schedule
 */

// @lc code=start
class Solution {
    enum Status {
        NOT_VISITED, VISITED,;
    }

    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> list = new ArrayList<>(numCourses);
        for (int i = 0; i < numCourses; i++) {
            list.add(new ArrayList<Integer>());
        }
        for (int[] p : prerequisites) {
            int prerequisite = p[1];
            int course = p[0];
            list.get(course).add(prerequisite);
        }
        Status[] visited = new Status[numCourses];

        for (int i = 0; i < numCourses; i++) {
            // if there is a cycle, return false
            if (!dfs(list, visited, i))
                return false;
        }
        return true;

    }

    private boolean dfs(List<List<Integer>> list, Status[] visited, int cur) {
        if (list.get(cur).isEmpty())
            return true;
        if (visited[cur] == Status.VISITED)
            return false;
        visited[cur] = Status.VISITED;

        for (int next : list.get(cur)) {
            if (!dfs(list, visited, next))
                return false;
        }

        visited[cur] = Status.NOT_VISITED;
        list.set(cur, new ArrayList<>());
        return true;
    }
}
// @lc code=end
