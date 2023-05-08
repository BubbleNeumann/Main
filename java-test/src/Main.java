import java.util.ArrayList;
import java.util.Arrays;

public class Main{
    public static void main(String[] args) {
        System.out.println("-- Task " + args[0] + " --");
        switch (args[0]) {
            case "1":
                Task1 task1 = new Task1(Arrays.copyOfRange(args, 1, args.length));
                System.out.println("avg " + task1.calcAvg());
                System.out.println("min " + task1.calcMin());
                System.out.println("max " + task1.calcMax());
                break;
            case "2":
                Task2 task2 = new Task2(Integer.parseInt(args[1]), Integer.parseInt(args[2]));
                Task2.transpose(task2).print();
                break;
            case "4":
                System.out.println(Task4.countCharOccurrences(args[1].charAt(0), args[2]));
                break;
            case "9":
                System.out.println(Arrays.toString(Task9.getObjMethods(new Task2())));
                break;
            case "10":
                ArrayList<Float> arr = new ArrayList<>(Arrays.asList(1f, 5f, 3f));
                System.out.println(new Task10<>(arr).getMaxValue());
                break;
            case "14":
                Task14.get().setVal(4.5);
                Task14.get().mul(2);
                System.out.println(Task14.get().getVal());
                break;
            default:
                System.out.println("no impl for this task");
        }
    }
}
