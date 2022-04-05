import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Main {
    static int N, M, count;
    static int map[][];
    static int dy[] = { -1, 0, 1, 0 }; // 북동남서
    static int dx[] = { 0, 1, 0, -1 };
    static int cnt = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stk = new StringTokenizer(br.readLine());
        N = Integer.parseInt(stk.nextToken());
        M = Integer.parseInt(stk.nextToken());
        map = new int[N][M];

        stk = new StringTokenizer(br.readLine());
        int r = Integer.parseInt(stk.nextToken());
        int c = Integer.parseInt(stk.nextToken());
        int d = Integer.parseInt(stk.nextToken());

        for (int i = 0; i < N; i++) {
            stk = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                map[i][j] = Integer.parseInt(stk.nextToken());
            }
        }

        clean(r, c, d);
        System.out.println(cnt);
    }

    // 0 1 2 3 북 동 남 서
    private static void clean(int r, int c, int d) {
        if (map[r][c] == 0) {
            map[r][c] = 2;
            cnt++;
        }
        boolean flag = false;

        for (int i = 0; i < 4; i++) {
            d = roation(d);
            int nr = r + dy[d];
            int nc = c + dx[d];
            if (map[nr][nc] == 0) {
                clean(nr, nc, d);
                flag = true;
                break;
            }
        }
        if (!flag) {
            d = roation(d);
            d = roation(d);
            int br = r + dy[d];
            int bc = c + dx[d];
            if (map[br][bc] == 1) {
                return;
            }
            d = roation(d);
            d = roation(d);
            clean(br, bc, d);
        }

    }

    private static int roation(int d) {
        return (d + 3) % 4;
    }
}
