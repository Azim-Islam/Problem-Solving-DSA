import java.io.BufferedWriter;
import java.io.BufferedReader;
import java.io.PrintWriter;
// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
public class WelcomeToJava {
    public static void main(String[] args) {
        PrintWriter pw = new PrintWriter(System.out);
        pw.println("Hello, World.\n" +
                "Hello, Java.");

        pw.flush();
        pw.close();
        }
    }