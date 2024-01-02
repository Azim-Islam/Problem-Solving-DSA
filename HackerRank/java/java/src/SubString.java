import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class SubString {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);
        String s1 = in.readLine();

        List<Integer> s = Stream.of(in.readLine().trim().split(" "))
                .map(Integer::parseInt)
                .collect(Collectors.toList());
        Integer start, end;
        start = s.get(0);
        end = s.get(1);

        out.println(s1.substring(start, end));

        out.flush();
        out.close();

    }
}
