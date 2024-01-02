import java.io.*;
import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class TrafficLights {
    static PrintWriter out = new PrintWriter(System.out);
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {

        ArrayList<Integer> l1 = (ArrayList<Integer>) Stream.of(in.readLine().split(" ")).map(Integer::parseInt)
                .collect(Collectors.toList());

        int streetLength = l1.get(0);
        int lightNum = l1.get(1);

        // Using an array to read values since we can't get values from sets in
        // Java
        int[] opArray = new int[lightNum];
        NavigableSet<Integer> streetPositions = new TreeSet<>();
        // Initialize the set with beginning and ending values
        streetPositions.add(0);
        streetPositions.add(streetLength);
        ArrayList<Integer> l2 = (ArrayList<Integer>) Stream.of(in.readLine().split(" ")).map(Integer::parseInt)
                .collect(Collectors.toList());
        for (int i = 0; i < lightNum; i++) {
            int nextTrafficLight = l2.get(i);
            opArray[i] = nextTrafficLight;
            streetPositions.add(nextTrafficLight);
        }

        int[] gapsArray = new int[lightNum];
        int prev = 0;
        int maxGap = 0;
        // Find the longest passage once all the streetlights are added
        for (int i : streetPositions) {
            maxGap = Math.max(i - prev, maxGap);
            prev = i;
        }

        gapsArray[lightNum - 1] = maxGap;
        /*
         * Remove the streetlights in reverse order to how they were added,
         * then find the gap created by removing each. Find the biggest
         * current gap, and add it to the next lowest index in answer.
         */
        for (int i = lightNum - 1; i > 0; i--) {
            streetPositions.remove(opArray[i]);
            int low = streetPositions.lower(opArray[i]);
            int high = streetPositions.higher(opArray[i]);
            maxGap = Math.max(maxGap, high - low);
            gapsArray[i - 1] = maxGap;
        }

        // Use StringBuilder to print out the array quicker
        StringBuilder sb = new StringBuilder();
        for (int i : gapsArray) {
            sb.append(i).append(" ");
        }
        out.println(sb);
        out.flush();
        out.close();
    }

    // BeginCodeSnip{Kattio}
    static class Kattio extends PrintWriter {
        private BufferedReader r;
        private StringTokenizer st;

        // standard input
        public Kattio() {
            this(System.in, System.out);
        }

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
            } catch (Exception e) {
            }
            return null;
        }

        public int nextInt() {
            return Integer.parseInt(next());
        }

        public double nextDouble() {
            return Double.parseDouble(next());
        }

        public long nextLong() {
            return Long.parseLong(next());
        }
    }
    // EndCodeSnip
}