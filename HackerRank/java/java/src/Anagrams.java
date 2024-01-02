import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.Arrays;

public class Anagrams {
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static  PrintWriter out = new PrintWriter(System.out);
    public static void main(String[] args) throws IOException {
        char[] s1 = in.readLine().trim().toLowerCase().toCharArray();
        char[] s2 = in.readLine().trim().toLowerCase().toCharArray();
        Arrays.sort(s1);
        Arrays.sort(s2);
        boolean f = true;
        if (s1.length == s2.length){
            for(int i = 0; i < s1.length; i++) {
                if (s1[i] != s2[i]) {
                    out.println("Not Anagrams");
                    f = false;
                    break;
                }
            }
            if (f){
                out.println("Anagrams");
            }
        }
        else{
            out.println("Not Anagrams");
        }
    out.flush(); out.close();
    }
}
