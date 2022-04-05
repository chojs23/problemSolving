import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Main {
    static int N;
    static int[] arr;
    static int[] oper = new int[4];
    static int max = Integer.MIN_VALUE;
    static int min = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        arr = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 4; i++)
            oper[i] = Integer.parseInt(st.nextToken());

        dfs(arr[0], 1);
        System.out.println(max);
        System.out.println(min);
    }

    private static void dfs(int num, int idx) {
        if (idx == N) {
            max = Math.max(max, num);
            min = Math.min(min, num);
            return;
        }
        for (int i = 0; i < 4; i++) {
            if (oper[i] > 0) {
                oper[i]--;
                if (i == 0) {
                    dfs(num + arr[idx], idx + 1);
                } else if (i == 1) {
                    dfs(num - arr[idx], idx + 1);
                } else if (i == 2) {
                    dfs(num * arr[idx], idx + 1);
                } else {
                    dfs(num / arr[idx], idx + 1);
                }
                oper[i]++;
            }
        }
    }
}
