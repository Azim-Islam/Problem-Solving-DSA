import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.regex.Pattern;

public class SyntaxChecker {
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(in.readLine().trim());
        for(int i = 0; i < n; i++){
            String s = in.readLine().trim();
            try{
            Pattern.compile(s);
            out.println("Valid");
            }catch (Exception e){
                out.println("Invalid");
            }

        }
        out.flush();
        out.close();
    }
}
