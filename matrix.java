//import java.lang.Throwable;

class Matrix {

    private int row, col;
    private int body[][];

    // default constructor
    public Matrix() {

        final int ROW = 2;
        final int COL = 2;

        row = ROW;
        col = COL;

        this.body = new int[row][col];

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                body[i][j] = i+j;
            }
        }
    }
    
    public Matrix multiply(Matrix multiplicand) throws Exception {

        if (this.col != multiplicand.row) {
            throw new ArithmeticException("Impossible to multiply");
        }

        Matrix product = new Matrix();

        for (int i = 0; i < product.row; i++) {
            for (int j = 0; j < product.col; j++) {
                product.body[i][j] = 0;
                for (int k = 0; k < this.row; k++) {
                    product.body[i][j] += this.body[i][k]*multiplicand.body[k][j];
                }            
            }
        }

        return product;        
    }

    public void print() {

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                System.out.print(body[i][j]);
            }
            System.out.println();
        }
    }
}

class Main {

    public static void main(String[] args) throws Exception {
        
        Matrix mx1 = new Matrix();
        Matrix mx2 = new Matrix();
        mx1.multiply(mx2).print();
    }
}
