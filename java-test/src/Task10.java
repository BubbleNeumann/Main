import java.util.ArrayList;

public class Task10<T extends Number> {
//    T[] arr;
    ArrayList<T> arr;

    public Task10(ArrayList<T> refArr) {
        arr = refArr;
    }

    public double getMaxValue() throws RuntimeException {
        if (arr.size() == 0) {
            throw new RuntimeException("empty array");
        }

        double max = arr.get(0).doubleValue();
        for (T e : arr) {
            if (e.doubleValue() > max) {
                max = e.doubleValue();
            }
        }

        return max;
    }

}
