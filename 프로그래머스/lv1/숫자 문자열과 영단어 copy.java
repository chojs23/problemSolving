package 프로그래머스.lv1;

import java.util.*;

class test {

    public static void main(String[] args) {
        System.out.println(solution("one4seveneight"));
    }

    private static int solution(String s) {
        int answer = 0;

        HashMap<String, String> word = new HashMap<>() {
            {
                put("zero", "0");
                put("one", "1");
                put("two", "2");
                put("three", "3");
                put("four", "4");
                put("five", "5");
                put("six", "6");
                put("seven", "7");
                put("eight", "8");
                put("nine", "9");
            }
        };
        for (String w : word.keySet()) {
            if (s.contains(w)) {
                s = s.replace(w, word.get(w));
            }
        }

        answer = Integer.parseInt(s);
        return answer;
    }

}