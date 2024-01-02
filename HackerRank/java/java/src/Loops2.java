import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Objects;
import java.util.stream.*;


public class Loops2 {
    public static void main(String[] args) throws Exception{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);

        int q = Integer.parseInt(in.readLine().trim());
        List<String> ans = new ArrayList<>();
        IntStream.range(0, q).forEach(tItr -> {
            try {
                List<String> tmp = new ArrayList<>();
                List<Integer> arr = Stream.of(in.readLine().trim().split(" ")).map(Integer::parseInt).collect(Collectors.toList());
                int a = arr.get(0);
                int b = arr.get(1);
                int n = arr.get(2);

                int s = a;
                for(int i = 0; i < n; i++){
                    s += (int) (Math.pow(2, i) * b);
                    tmp.add(s+"");
                }
                ans.add(String.join(" ", tmp));
            } catch (IOException e) {
                throw new RuntimeException(e);
            }

        });
        out.println(String.join("\n", ans));
        out.flush();
        out.close();

    }
}
