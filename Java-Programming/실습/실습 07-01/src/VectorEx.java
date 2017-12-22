/**
 * @date : 2017. 5. 24.
 */
/**
 * <pre>
 *  
 *    |_ VectorEx.java
 * 
 * </pre>
 * @date : 2017. 5. 24. ¿ÀÈÄ 6:24:14
 * @version : 
 * @author : Jho
 */

import java.util.*;

public class VectorEx {
    public static void main(String args[]) {
        Scanner scan = new Scanner(System.in);

        Vector<Double> list = new Vector<Double>();

        // input numbers in a list
        System.out.print("Enter 10 real numbers >> ");
        for (int i = 0; i < 10; i++)
            list.add(scan.nextDouble());

        // find a biggest one
        double biggest = list.elementAt(0);
        for (int i = 1; i < 10; i++)
            if (biggest < list.elementAt(i))
                biggest = list.elementAt(i);

        // print
        System.out.println("Biggest number : " + biggest);
    }

}
