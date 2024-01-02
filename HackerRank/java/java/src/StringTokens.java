import java.io.*;
import java.util.StringTokenizer;
public class StringTokens {
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        String s = in.readLine().trim();
        StringTokenizer tkn = new StringTokenizer(s, "[A-Z !,?._'@]+");
        out.println(tkn.countTokens());
        while(tkn.hasMoreTokens()){
            out.println(tkn.nextToken());
        }
        out.flush(); out.close();
    }

}
