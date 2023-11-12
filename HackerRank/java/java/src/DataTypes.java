import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.stream.IntStream;

public class DataTypes {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);

        IntStream.range(0, Integer.parseInt(in.readLine().trim())).forEach(itr -> {
            try {
                String v = in.readLine().trim();
                try{
                    Long t = Long.parseLong(v);
                    out.println(v+" can be fitted in:");
                    if (t >= Byte.MIN_VALUE && t <= Byte.MAX_VALUE) {
                        out.println("* byte");
                    }
                    if (t >= Short.MIN_VALUE && t <= Short.MAX_VALUE) {
                        out.println("* short");
                    }
                    if (t >= Integer.MIN_VALUE && t <= Integer.MAX_VALUE) {
                        out.println("* int");
                    }
                    if (t >= Long.MIN_VALUE && t <= Long.MAX_VALUE) {
                        out.println("* long");
                    }
                }
                catch (Exception e) {
                    out.println(v+" can't be fitted anywhere.");
                }
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        });
        out.flush();
        out.close();




    }
}
