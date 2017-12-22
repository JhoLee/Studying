/**
 * @date : 2017. 5. 25.
 */
/**
 * <pre>
 *  
 *    |_ Example.java
 * 
 * </pre>
 * @date : 2017. 5. 25. 오전 10:37:42
 * @version : 
 * @author : Jho
 */

import java.util.*;

public class Example {

    public static void main(String[] args) {
        ArrayList<Double> a = new ArrayList<Double>();

        for (int i = 0; i < 20; i++) {
            double d = Math.random() * 100; // 0.0 ~ 100.0 사이의 랜덤한 실수
            a.add(d);
        }
        Iterator<Double> it = a.iterator();

        while (it.hasNext())
            System.out.println(it.next());
    }
}