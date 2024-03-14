import java.io.*;
import java.util.*;


public class MovieTickets2{
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    static TreeMap<Integer, Integer> table = new TreeMap<>();
    static void add(int x) {

        if (table.containsKey(x)) {

            table.put(x, table.get(x) + 1);

        } else {

            table.put(x, 1);

        }

    }


    static void remove(int x) {

        table.put(x, table.get(x) - 1);

        if (table.get(x) == 0) { table.remove(x); }

    }

    public static void main(String[] args) throws IOException {
//        StringTokenizer st = new StringTokenizer(in.readLine());
         FastIO io = new FastIO();
//        Integer n = Integer.parseInt(st.nextToken());
//        Integer k = Integer.parseInt(st.nextToken());
        int n = io.nextInt();
		int k = io.nextInt();

        List<List<Integer>> arr = new ArrayList<>();

        for(int i = 0; i < n; i++){
//            StringTokenizer st1 = new StringTokenizer(in.readLine());
//            int a = Integer.parseInt(st1.nextToken());
//            int b = Integer.parseInt(st1.nextToken());
            arr.add(List.of(io.nextInt(), io.nextInt()));
        }

        arr.sort(Comparator.comparing(list -> list.get(1)));


        table.put(0, k);
        int c = 0;

        for(int i = 0; i < n; i++){
            int a = arr.get(i).get(0);
            int b = arr.get(i).get(1);
            Integer idx = table.floorKey(a);

            if (idx != null){
                c += 1;
                remove(idx);
                add(b);
            }

        }
        out.println(c);
        out.flush();

    }
    static class FastIO extends PrintWriter {

		private InputStream stream;

		private byte[] buf = new byte[1 << 16];

		private int curChar, numChars;


		// standard input

		public FastIO() { this(System.in, System.out); }

		public FastIO(InputStream i, OutputStream o) {

			super(o);

			stream = i;

		}

		// file input

		public FastIO(String i, String o) throws IOException {

			super(new FileWriter(o));

			stream = new FileInputStream(i);

		}


		// throws InputMismatchException() if previously detected end of file

		private int nextByte() {

			if (numChars == -1) throw new InputMismatchException();

			if (curChar >= numChars) {

				curChar = 0;

				try {

					numChars = stream.read(buf);

				} catch (IOException e) { throw new InputMismatchException(); }

				if (numChars == -1) return -1;  // end of file

			}

			return buf[curChar++];

		}


		// to read in entire lines, replace c <= ' '

		// with a function that checks whether c is a line break

		public String next() {

			int c;

			do { c = nextByte(); } while (c <= ' ');

			StringBuilder res = new StringBuilder();

			do {

				res.appendCodePoint(c);

				c = nextByte();

			} while (c > ' ');

			return res.toString();

		}

		public int nextInt() {  // nextLong() would be implemented similarly

			int c;

			do { c = nextByte(); } while (c <= ' ');

			int sgn = 1;

			if (c == '-') {

				sgn = -1;

				c = nextByte();

			}

			int res = 0;

			do {

				if (c < '0' || c > '9') throw new InputMismatchException();

				res = 10 * res + c - '0';

				c = nextByte();

			} while (c > ' ');

			return res * sgn;

		}

		public double nextDouble() { return Double.parseDouble(next()); }

	}
}
