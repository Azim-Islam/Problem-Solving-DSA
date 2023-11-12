import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;

public class StringIntroduction {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);

        String s1 = in.readLine();
        String s2 = in.readLine();

        out.println(s1.length()+s2.length());

        if (s1.compareTo(s2) > 0) out.println("Yes");
        else out.println("No");

        out.println(String.valueOf(s1.charAt(0)).toUpperCase()+s1.substring(1) + " "+
                String.valueOf(s2.charAt(0)).toUpperCase()+s2.substring(1));

        out.flush();
        out.close();


    }
}
