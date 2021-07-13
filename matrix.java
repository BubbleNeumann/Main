import java.util.Scanner;
import java.util.InputMismatchException;

class Matrix {

    private int row, col;
    private int* body;
    
    // used by several constructors
    private static int* fillMatrix(int row, int col) {
        
        Scanner scanner = new Scanner(System.in);
        
        int* body = new int[row*col];
        while(row--) {
            
            // get a string, then parse, then fill an array
            
        }
    }
    
    // used only by default constructor
    // do I need this method?? or it might be moved into default constructor's body
    private static int getDimension(String message) {
        
        Scanner scanner = new Scanner(System.in);
        boolean excCaught;
        
        int value;

        do {
            
            excCaught = false;
            try {
              
                System.out.println(message);
                value = scanner.nextInt();
                
            } catch(InputMismatchException e) {
              
                excCaught = true;
                System.out.println("try again");
                
                // move the scanner onto the next line 
                // unless it becames an infinite loop
                scanner.next();
            }
            
        } while (excCaught);
        scanner.close();
        
        return value;
    }

    // default constructor
    public Matrix() {
        
        row = getDimension("Number of rows?");
        col = getDimension("Number of columns?");
        body = fillMatrix(row, col);
    }
    
    // initialization constructor 
    public Matrix(int row, int col) {
        this.row = row;
        this.col = col;
        body = fillMatrix(row, col);
    }
    
    public Matrix matrixMultiplication( Matrix& multiplicand) {
        
        Matrix result = new Matrix();
        
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
        
        Matrix mx1 = new Matrix();
        Matrix mx2 = new Matrix();

    }
}
