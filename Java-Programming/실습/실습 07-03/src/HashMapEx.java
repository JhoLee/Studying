/**
 * @date : 2017. 5. 24.
 */

/**
 * <pre>
 *  
 *    |_ HashMapEx.java
 * 
 * </pre>
 * @date : 2017. 5. 24. 오후 6:55:20
 * @version : 
 * @author : Jho
 */
import java.util.*;

public class HashMapEx {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        HashMap<String, Integer> nations = new HashMap<String, Integer>();

        // Input
        System.out.println("나라 이름과 인구를 입력하세요 (Ex. Korea, 12345)");
        for (int i = 0; i < 10; i++) {
            System.out.print((i + 1) + "번째 나라 >> ");
            nations.put(scan.next(), scan.nextInt());
        }

        //
        System.out.print("인구를 출력하고자 하는 나라의 이름을 입력하세요 >> ");
        String key = scan.next();
        int value = 0;
        value = nations.get(key);
        System.out.println(key + ": " + value + "명");
    }

}
