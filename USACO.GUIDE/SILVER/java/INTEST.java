import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.List;
import java.util.concurrent.atomic.AtomicReference;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class INTEST {
    static PrintWriter out = new PrintWriter(System.out);
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        List<Integer> nn = Stream.of(in.readLine().split(" ")).map(Integer::parseInt).collect(Collectors.toList());
        Integer n = nn.get(0);
        Integer k = nn.get(1);
        AtomicReference<Integer> c = new AtomicReference<>(0);
        IntStream.range(0, n).forEach(itr -> {
            try {
                Integer t = Integer.parseInt(in.readLine());
                if (t%k == 0){
                    c.updateAndGet(v -> v + 1);
                }
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        });

        out.println(c);
        out.flush();
        out.close();
    }
}
