/**
 * @date : 2017. 5. 24.
 */

/**
 * <pre>
 *  
 *    |_ HashMapEx.java
 * 
 * </pre>
 * @date : 2017. 5. 24. ���� 6:55:20
 * @version : 
 * @author : Jho
 */
import java.util.*;

public class HashMapEx {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        HashMap<String, Integer> nations = new HashMap<String, Integer>();

        // Input
        System.out.println("���� �̸��� �α��� �Է��ϼ��� (Ex. Korea, 12345)");
        for (int i = 0; i < 10; i++) {
            System.out.print((i + 1) + "��° ���� >> ");
            nations.put(scan.next(), scan.nextInt());
        }

        //
        System.out.print("�α��� ����ϰ��� �ϴ� ������ �̸��� �Է��ϼ��� >> ");
        String key = scan.next();
        int value = 0;
        value = nations.get(key);
        System.out.println(key + ": " + value + "��");
    }

}
