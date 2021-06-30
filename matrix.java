import java.util.Scanner;

// for graphical interfaces
// import javax.swing.JOptionPane;

class Main 
{
  public static void main(String[] args) 
  {
    
    // String name = JOptionPane.showInputDialog("Enter your name");
    // JOptionPane.showMessageDialog(null, "hello "+name);
    
    // int age = Integer.parceInt(JOptionPane.showinputDialog("Enter your age"))
    // JOptionPane.showMessageDialog(null, "yyou are "+age+"years old");
    
    Scanner scanner = new Scanner(System.in);
    
    System.out.println("Number of the rows? ");
    int row = scanner.nextInt();
    
    System.out.println("Number of the columns? ");
    int col = scanner.nextInt();
    
    System.out.println(row);
    System.out.println(col);
    
    int[] mx = new int[row*col];
    
    // String[][] cars = new String[3][3];
    // cars[0][0] = "Mustang";
    
    // boolean result = name.equalsIgnoreCase("smth");
    // int result = name.length();
    
    for(int i = row*col; i--;)
    {
      // fill an array
    }
    
    scanner.close();
  }
} 
