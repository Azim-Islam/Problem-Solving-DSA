import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;

public class StringReverse {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);

        StringBuilder s2 = new StringBuilder(in.readLine().trim());
        StringBuilder s1 = new StringBuilder(s2);

        String v = (s2.compareTo(s1.reverse()) == 0) ? "Yes":"No";
        out.println(v);


        out.flush();
        out.close();

    }
}
