import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;

public class EndofFile {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);
        int i = 1;
        String s;
        while((s = in.readLine()) != null){
            out.println(i+" "+s);
            i++;
        }

        out.flush();
        out.close();

    }
}
