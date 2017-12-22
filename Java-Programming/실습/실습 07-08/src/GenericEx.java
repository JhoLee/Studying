/**
 * @date : 2017. 5. 26.
 */
/**
 * <pre>
 *  
 *    |_ GenericEx.java
 * 
 * </pre>
 * 
 * @date : 2017. 5. 26. ¿ÀÀü 9:00:43
 * @version :
 * @author : Jho
 */

class MyClass<E> {
    private E e;

    public MyClass(E e) {
        this.e = e;
    }

    void set(E e) {
        this.e = e;

    }

    E get() {
        return e;
    }
}

public class GenericEx {
    public static void main(String[] args) {
        MyClass<String> s = new MyClass<String>("Hello");

        System.out.println(s.get());
        s.set("Hi");
        System.out.println(s.get());
    }
}
