import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.PrintWriter;
// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
public class StdinStdout {
    public static void main(String[] args) throws java.io.IOException{
        PrintWriter pw = new PrintWriter(System.out);
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));


        for(int i = 0; i < 3; i++){
            pw.println(input.readLine());
        }
        pw.flush();
        pw.close();
        }
    }