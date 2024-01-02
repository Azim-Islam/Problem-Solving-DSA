import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.Scanner;

class StdinStdout2{
    public static void main(String[] args) throws Exception{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter print = new PrintWriter(System.out);

        int i = Integer.parseInt(input.readLine().trim());
        double f = Double.parseDouble(input.readLine().trim());
        String s = input.readLine().trim();
        print.println(String.format("String: %s", s));
        print.println("Double: "+ f);
        print.println(String.format("Int: %d", i));

        print.flush();
        print.close();
    }
}