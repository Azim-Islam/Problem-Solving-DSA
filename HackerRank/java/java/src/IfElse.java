import java.io.InputStream;
import java.io.InputStreamReader;
import  java.io.PrintWriter;
import  java.io.BufferedReader;
import java.util.function.LongBinaryOperator;

class IfElse{
    public  static  void  main(String args[]) throws Exception{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter print = new PrintWriter(System.out);

        long n = Long.parseLong(input.readLine().trim());

        if (n%2 == 1){
            print.println("Weird");
        } else if (n >= 2 && n <= 5) {
            print.println("Not Weird");
        } else if (n >= 6 &&  n <= 20) {
            print.println("Weird");
        }
        else {
            print.println("Not Weird");
        }


        print.flush();
        print.close();

    }
}