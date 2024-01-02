import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.*;




public class Solution {
    static PrintWriter out = new PrintWriter(System.out);
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    public static  void main(String[] args) throws IOException {
        int n = Integer.parseInt(in.readLine());
        List<List<Integer>> arr = new ArrayList<>();
        int x, y;
        //
        long T0 = System.currentTimeMillis();
        for(int i =0; i<n; i++){
            StringTokenizer st = new StringTokenizer(in.readLine());
            x = Integer.parseInt(st.nextToken());
            y = Integer.parseInt(st.nextToken());
            arr.add(Arrays.asList(x, y));
        }



        long T1 = System.currentTimeMillis();
//        System.out.println("Runtime for Input:"+ (T1-T0));


        T0 = System.currentTimeMillis();
        arr.sort(Comparator.comparing(o -> o.get(1)));
        T1 = System.currentTimeMillis();
//        System.out.println("Runtime for Sorting:"+ (T1-T0));


        T0 = System.currentTimeMillis();
        Integer f = arr.get(0).get(1);
        Integer c = 1;

        for (List<Integer> e: arr.subList(1, n)) {
            if (e.get(0) >= f){
                c += 1;
                f = e.get(1);
            }
        }

        out.println(c);
        T1 = System.currentTimeMillis();
//        System.out.println("Runtime for Output:"+ (T1-T0));
        out.flush();

    }
}
