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
        double sum = 0;
        for (double e : this.args) {
            sum += e;
        }

        return sum / this.args.length;
    }

    public double calcMin() {
        double min = this.args[0];
        for (int i = 1; i < this.args.length; ++i) {
            if (this.args[i] < min) {
                min = this.args[i];
            }
        }
        return min;
    }

    public double calcMax() {
        double max = this.args[0];
        for (int i = 1; i < this.args.length; ++i) {
            if (this.args[i] > max) {
                max = this.args[i];
            }
        }
        return max;
    }
}
