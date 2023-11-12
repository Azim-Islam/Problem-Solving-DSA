import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;

public class IntToString {
    public static void main(String[] arg) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);

        int n = Integer.parseInt(in.readLine().trim());
        if (n >= -100 && n <= 100){
            out.println("Good job");
        }
        else{
            out.println("Wrong answer");
        }


        out.flush();
        out.close();
    }
}
