import java.util.Scanner;
import java.util.InputMismatchException;

class Matrix {

    private int row, col;
    private int body[];

    // default constructior
    public Matrix() {
        
        Scanner scanner = new Scanner(System.in);
        boolean excCaught;

        do {

            excCaught = false;

            try {
              
                System.out.println("Number of rows?");
                row = scanner.nextInt();
                
                System.out.println("Number of columns?");
                col = scanner.nextInt();
            } catch(InputMismatchException e) {
              
                excCaught = true;
                System.out.println("try again");
                scanner.next();
            }

        } while (excCaught);
        scanner.close();
    }
  
    // the determinant is a scalar value that is a function of the entries of a square matrix
    public int calcDeterminant() {
        
        int det;
        
        if (row != col) det = 0;
        
        return det;
    }
    
    // rank of a matrix A is the dimension of the vector space generated (or spanned) by its columns 
    public int calcRank() {
        
        int rank(0);
        return rank;
    }

    public void printMatrix() {
        
        for (int i = row; i > 0 ; i--) {
            for (int j = col; j > 0; j--) {
                System.out.print(body[(row-i)*col + col-j]);
            }
        }
    }
}

public class Main {

    public static void main(String[] args) {
        
        Matrix mx = new Matrix();

    }
}
