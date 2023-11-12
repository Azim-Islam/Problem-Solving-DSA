import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.time.LocalDate;
import java.util.List;
import java.util.Locale;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class DateTime {
    public  static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);

        List<Integer> date = Stream.of(in.readLine()
                            .trim().split(" "))
                            .map(Integer::parseInt)
                            .collect(Collectors.toList());

        LocalDate dd = LocalDate.of(date.get(2), date.get(0), date.get(1));
        out.println(dd.getDayOfWeek().toString().toUpperCase());

        out.flush();
        out.close();

    }
}
