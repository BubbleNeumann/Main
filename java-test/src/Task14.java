// singletons babyyy
public class Task14 {
    private static Task14 singleton;
    private double val;
    private boolean initialized;

    private Task14(double val) {
        if (singleton == null) {
            this.val = val;
            singleton = this;
            initialized = false;
        }
    }

    public static Task14 get() {
        if (singleton == null) {
            singleton = new Task14(0);
        }
        return singleton;
    }

    public double getVal() {
        if (!singleton.initialized) {
            throw new RuntimeException("val wasn't set");
        }
        return val;
    }

    public void setVal(double val) {
        singleton.val = val;
        singleton.initialized = true;
    }

    public void mul(double val) {
        if (!singleton.initialized) {
            throw new RuntimeException("val wasn't set");
        }
        singleton.val *= val;
    }
}
