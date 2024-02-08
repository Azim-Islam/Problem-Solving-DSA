import java.io.*;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.StringTokenizer;
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

public class SoloLeveling {


    public static void main(String args[]) throws IOException {
        Kattio io = new Kattio();
        int t = io.nextInt();

        int N, P, X, A;

        for(int tt = 0 ; tt < t; tt++){
            ArrayList<Integer> arr = new ArrayList<Integer>();
            PriorityQueue<Integer> pq = new PriorityQueue<>();


            N = io.nextInt();
            P = io.nextInt();
            X = io.nextInt();
            A = io.nextInt();

            P = P + X;


            for(int i = 0; i < N; i++){
                arr.add(io.nextInt());
            }

            int i = 0;

            for(i=0; i < N; i++){
                if (pq.size() < A){
                    pq.add(arr.get(i));
                }
                else{
                    pq.add(arr.get(i));
                    int v = pq.peek();
                    pq.poll();
                    if (P - v < 0){
                        break;
                    }
                    P -= v;

                }
            }
            io.println(i);



        }
        io.close();

    }
}
