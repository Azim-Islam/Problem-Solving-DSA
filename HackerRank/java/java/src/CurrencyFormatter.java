import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.text.NumberFormat;
import java.util.Locale;

public class CurrencyFormatter {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);

        double v = Double.parseDouble(in.readLine()
                        .trim());

        char rs = (char) 8377;
        char yen = (char) 165;
        char corr_yen = (char) 65509;

        char c1 = (char) 239;
        char c2 = (char) 191;
        char c3 = (char) 194;
        char c4 = (char) 226;
        char c5 = (char) 172;


        NumberFormat currencyFormat = NumberFormat.getCurrencyInstance(Locale.US);
        String formattedAmount = currencyFormat.format(v);
        out.println("US: "+ formattedAmount);

        currencyFormat = NumberFormat.getCurrencyInstance(new Locale("en", "IN"));
        formattedAmount = currencyFormat.format(v);
        out.println("India: "+ formattedAmount);

        currencyFormat = NumberFormat.getCurrencyInstance(Locale.CHINA);
        formattedAmount = currencyFormat.format(v);
        out.println("China: "+ formattedAmount);

        currencyFormat = NumberFormat.getCurrencyInstance(Locale.FRANCE);
        formattedAmount = currencyFormat.format(v);
        out.println("France: "+ formattedAmount);



        out.flush();
        out.close();
    }
}
