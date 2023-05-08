import java.util.Arrays;

// Matrix class
public class Task2 {

    int rowCount;
    int colCount;
    double[][] matrix;

    public Task2() {
        rowCount = 0;
        colCount = 0;
    }

    public Task2(int rowCount, int colCount) {
        this.rowCount = rowCount;
        this.colCount = colCount;
        matrix = new double[rowCount][colCount];
        String[] lineElems;
        for (int i = 0; i < rowCount; ++i) {
            lineElems = System.console().readLine().trim().split("\\s+");
            for (int j = 0; j < colCount; ++j) {
                matrix[i][j] = Double.parseDouble(lineElems[j]);
            }
        }
    }

    public static Task2 transpose(Task2 matr) {
        Task2 transposed = new Task2();
        transposed.rowCount = matr.colCount;
        transposed.colCount = matr.rowCount;
        transposed.matrix = new double[transposed.rowCount][transposed.colCount];
        for (int i = 0; i < matr.rowCount; ++i) {
            for (int j = 0; j < matr.colCount; ++j) {
                transposed.matrix[i][j] = matr.matrix[j][i];
            }
        }

        return transposed;
    }

    public void print() {
        for (double[] row : matrix) {
            System.out.println(Arrays.toString(row));
        }
    }
}
