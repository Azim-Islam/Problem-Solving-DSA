import java.util.Scanner;

public class SubStringComparisons {

    public static String getSmallestAndLargest(String s, int k) {
        String smallest = s;
        String largest = "";
        for(int i=0; i+k <= s.length(); i++) {
            String substring = s.substring(i, i + k);
            smallest = (smallest.compareTo(substring) > 0) ? substring : smallest;
            largest = (largest.compareTo(substring) < 0) ? substring : largest;
        }

        // Complete the function
        // 'smallest' must be the lexicographically smallest substring of length 'k'
        // 'largest' must be the lexicographically largest substring of length 'k'
        
        return smallest + "\n" + largest;
    }


    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        int k = scan.nextInt();
        scan.close();
      
        System.out.println(getSmallestAndLargest(s, k));
    }
}