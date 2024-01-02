import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;

public class Loops1 {
    public  static void main(String[] args) throws Exception{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);

        int n = Integer.parseInt(in.readLine().trim());
        for(int i = 1; i <= 10; i++){
            out.println(n+" x "+i+" = "+ n*i);
        }

        out.flush();
        out.close();
    }
}
