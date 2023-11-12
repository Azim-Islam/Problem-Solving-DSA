import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;

public class StaticInitializer {
    static int B = 0;
    static  int H = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);


        int b = Integer.parseInt(in.readLine().trim());
        int h = Integer.parseInt((in.readLine()).trim());

        if (b > B && h > H){
            out.println(b*h);
        }
        else{
            out.println("java.lang.Exception: Breadth and height must be positive");
        }
        out.flush();
        out.close();
    }
}
