import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Task4 {
    public static long countCharOccurrences(char c, String filename) {
        long cnt = 0;
        try {
            BufferedReader in = new BufferedReader(new FileReader(filename));
            String line;
            while((line = in.readLine()) != null) {
                cnt += line.chars().filter(ch -> ch == c).count();
            }
            in.close();
        }
        catch (IOException e) {
            System.out.println("exception when reading file");
        }
        return cnt;
    }
}
