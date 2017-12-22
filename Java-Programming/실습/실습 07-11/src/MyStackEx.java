/**
 * @date : 2017. 5. 26.
 */
/**
 * <pre>
 *  
 *    |_ MyStackEx.java
 * 
 * </pre>
 * @date : 2017. 5. 26. ¿ÀÀü 11:01:54
 * @version : 
 * @author : Jho
 */

import java.util.*;

interface Stack<T> {
    T pop();

    boolean push(T ob);
}

class MyStack<T> implements Stack<T> {

    private int top;
    LinkedList<T> list = null;

    public MyStack() {
        top = -1;
        list = new LinkedList<T>();
    }

    @Override
    public T pop() {
        // TODO Auto-generated method stub
        if (isEmpty() == true)
            return null;
        else {
            T t = list.get(top);
            list.remove(top--);
            return t;
        }

    }

    @Override
    public boolean push(T ob) {
        // TODO Auto-generated method stub
        try {
            list.add(ob);
            top++;
        } catch (Exception e) {

            return false;
        }
        return true;

    }

    public boolean isEmpty() {
        if (top < 0)
            return true;
        else
            return false;
    }

}

public class MyStackEx {
    public static void main(String args[]) {
        Scanner scan = new Scanner(System.in);
        MyStack<Integer> iStack = new MyStack<Integer>();

        Loop1: while (true) {
            System.out.print("(1)push (2)pop (0)Exit.. >> ");
            int op = scan.nextInt();
            switch (op) {
            case 1: // push
                System.out.print("Enter a integer to push >> ");
                int num = scan.nextInt();
                if (iStack.push(num) == true)
                    System.out.println("Success!");
                else
                    System.out.println("ERROR");
                break;
            case 2: // pop
                if (iStack.isEmpty() == true)
                    System.out.println("The stack is empty...");
                else
                    System.out.println(iStack.pop());

                break;
            case 0: // Exit..
                break Loop1;
            default: // ERROR
                System.out.println("Wrong Input");
                break;
            }

        }

    }

}
