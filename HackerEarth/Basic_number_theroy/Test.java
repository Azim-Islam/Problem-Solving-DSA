import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
import java.lang.Math;
class Test {
    public static double x_1(int a, int s, int d){
        int x = (2*a-d)*(2*a-d);
        return (-(2*a - d) + Math.sqrt(x + 8*s*d))/(2*d);
    }
    public static void main(String args[] ) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());              

        int d = 2; int s = n;
        double v, s0;
        int count = 0;

        for(int i=1; i < n/2 + 2; i += 2){
            v = x_1(i, s, d);
            s0 = (v*(2*i + (v-1)*d))/2;
            System.out.println(i +" " + v + " " + s0);
            if(s0 == s && Math.floor(v) == v){
                count += 1;
            }
        }

        if(n%2 == 1){count += 1;}

        System.out.println(count);

    }
}
