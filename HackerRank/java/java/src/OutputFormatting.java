import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;

class OutputFormatting{
    public static void main(String[] args) throws  Exception{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter print = new PrintWriter(System.out);
        String line;
        print.println("================================");
        while((line = input.readLine()) != null) {
            String[] s = line.trim().split(" ");
            if (s.length == 2) {
                String ch = s[0];
                String i = s[1];
                String spaces = " ".repeat(Math.max(0, 15 - ch.length()));
                String zeros = "0".repeat(Math.max(0, 3 - i.length()));
                print.println(ch+ spaces +zeros+i);
            }
            else{
                break;
            }
        }
        print.println("================================");
        print.flush();
        print.close();
    }
}