import java.lang.reflect.Method;

public class Task9 {
    public static String[] getObjMethods(Object obj) {
        Method[] methods = obj.getClass().getMethods();
        String[] methodsNames = new String[methods.length];
        for (int i = 0; i < methods.length; ++i) {
            methodsNames[i] = methods[i].getName();
        }
        return methodsNames;
    }
}
