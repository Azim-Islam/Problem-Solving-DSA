import java.io.*;
import java.util.*;

import static java.lang.Long.min;

/**
 * Simple yet moderately fast I/O routines.
 * Some notes:
 *
 * - When done, you should always do io.close() or io.flush() on the
 *   Kattio-instance, otherwise, you may lose output.
 *
 * - The nextInt(), nextDouble(), and nextLong() methods will throw an
 *   exception if there is no more data in the input.
 *
 * @author: Kattis
 */

class Kattio extends PrintWriter {
	private BufferedReader r;
	private StringTokenizer st;
	// standard input
	public Kattio() { this(System.in, System.out); }
	public Kattio(InputStream i, OutputStream o) {
		super(o);
		r = new BufferedReader(new InputStreamReader(i));
	}
	// USACO-style file input
	public Kattio(String problemName) throws IOException {
		super(problemName + ".out");
		r = new BufferedReader(new FileReader(problemName + ".in"));
	}
	// returns null if no more input
	public String next() {
		try {
			while (st == null || !st.hasMoreTokens())
				st = new StringTokenizer(r.readLine());
			return st.nextToken();
		} catch (Exception e) {}
		return null;
	}
	public int nextInt() { return Integer.parseInt(next()); }
	public double nextDouble() { return Double.parseDouble(next()); }
	public long nextLong() { return Long.parseLong(next()); }
}

public class AppleOffer {
	public static void main(String[] args) {
		Kattio io = new Kattio();
        Long n = io.nextLong();
		Long m = io.nextLong();
		Long k = io.nextLong();
		Long r = io.nextLong();

        ArrayList<List<Long>> arr = new ArrayList<>();

        for(Long i = 0L; i < m; i ++){
            Long a = io.nextLong();
            Long b = io.nextLong();
            arr.add(Arrays.asList(a, b));
        }
        arr.sort(Comparator.comparingLong(a -> a.get(1)));
//        io.println(arr);
        Long v = 0L;
        for(List<Long> a : arr){
            v += min(r, a.get(0));
        }

        Long lagbe = n - v;
        Long ans = 0L;
        for(List<Long> a: arr){
            if(lagbe > 0){
                Long t = min(lagbe, min(k, r- min(r, a.get(0))));
                lagbe -= t;
                ans += t*a.get(1);
            }
        }

        if (lagbe <= 0){
            io.println(ans);
        }
        else{
            io.println("-1");
        }


		/*
		 * Make sure to include the line below, as it
		 * flushes and closes the output stream.
		 */
		io.close();
	}
}

