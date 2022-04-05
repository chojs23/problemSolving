import java.util.*;

class Solution {
    public int[] solution(int N, int[] stages) {
        int[] answer = new int[N];
        HashMap<Integer, Double> map = new HashMap<>();
        int deno = stages.length;

        for (int i = 1; i < N + 1; i++) {
            if (deno != 0) {
                int count = 0;
                for (int stage : stages) {
                    if (stage == i)
                        count = count + 1;
                }
                map.put(i, (double) count / deno);
                deno -= count;
            } else {
                map.put(i, (double) 0);
            }
        }

        List<Integer> keySetList = new ArrayList<>(map.keySet());
        Collections.sort(keySetList, (o1, o2) -> (map.get(o2).compareTo(map.get(o1))));
        int idx = 0;
        for (int key : keySetList) {
            answer[idx] = key;
            idx++;
        }

        return answer;
    }
}