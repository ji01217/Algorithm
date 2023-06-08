import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int t = scanner.nextInt();
        scanner.nextLine(); // 개행 문자 읽기

        for (int i = 0; i < t; i++) {
            String wave = scanner.nextLine();
            boolean result = checkPattern(wave);
            if (result) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }

        scanner.close();
    }

    private static boolean checkPattern(String wave) {
        String pattern = "(100+1+|01)+";
        Pattern regex = Pattern.compile(pattern);
        Matcher matcher = regex.matcher(wave);

        return matcher.matches();
    }
}