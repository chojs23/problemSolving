import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N];
        int answer = 1;
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        int last = arr[arr.length - 1];

        for (int i = arr.length - 1; i >= 0; i--) {
            if (arr[i] > last) {
                answer += 1;
                last = arr[i];
            }
        }
        System.out.println(answer);
    }
}