/**
 * @date : 2017. 5. 24.
 */

/**
 * <pre>
 *  
 *    |_ ArryListEx.java
 * 
 * </pre>
 * 
 * @date : 2017. 5. 24. 오후 6:43:01
 * @version :
 * @author : Jho
 */
import java.util.*;

public class ArryListEx {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        ArrayList<Character> list = new ArrayList<Character>();

        System.out.print("5개의 학점(A/B/C/D/F)을 '공백'으로 구분하여 입력하세요 >> ");
        for (int i = 0; i < 5; i++) {
            list.add(scan.next().charAt(0));
        }
        for (int i = 0; i < 5; i++) {
            System.out.print(point(list.get(i)) + " ");

        }

    }

    public static double point(char point) {
        switch (point) {
        case 'A':
            return 4.0;
        case 'B':
            return 3.0;
        case 'C':
            return 2.0;
        case 'D':
            return 1.0;
        case 'F':
            return 0;
        default:
            return -1;

        }
    }

}
