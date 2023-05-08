import java.util.Arrays;
import java.util.NoSuchElementException;

public class Task1 {
    double[] args;

    Task1(String[] args) throws RuntimeException {
        this.args = new double[args.length];
        for (int i = 0; i < this.args.length; ++i) {
            try {
                this.args[i] = Double.parseDouble(args[i]);
            }
            catch (Exception e) {
                throw new RuntimeException("invalid argument");
            }
        }
    }

    public double calcAvg() {
        return Arrays.stream(args).sum() / args.length;
    }

    public double calcMin() throws NoSuchElementException {
        return Arrays.stream(args).min().getAsDouble();
    }

    public double calcMax() throws NoSuchElementException {
        return Arrays.stream(args).max().getAsDouble();
    }
}
