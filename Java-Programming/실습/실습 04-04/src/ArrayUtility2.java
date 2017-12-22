/**
 * @date : 2017. 4. 4.
 */
/**
 * <pre>
 *  
 *    |_ ArrayUtility2.java
 * </pre>
 * 
 * @date : 2017. 4. 4. ¿ÀÀü 12:57:06
 * @version :
 * @author : Jho
 */

import java.util.Scanner;

public class ArrayUtility2
{
    static int[] concat(int[] s1, int[] s2)
    {
        int[] iTempAry1 = new int[s1.length + s2.length];

        for (int i = 0; i < s1.length; i++)
        {
            iTempAry1[i] = s1[i];
        }

        for (int i = 0; i < s2.length; i++)
        {
            iTempAry1[i + s1.length] = s2[i];
        }

        return iTempAry1;

    }

    static int[] remove(int[] s1, int[] s2)
    {
        int[] iTempAry2 = new int[s1.length];
        int num = 0;
        for (int i = 0; i < s1.length; i++)
        {
            int count = 0;
            for (int j = 0; j < s2.length; j++)
            {
                if (s1[i] == s2[j]) count += 1;
            }
            if (count == 0) iTempAry2[num++] = s1[i];

        }

        int[] iTempAry3 = new int[num];
        for (int i = 0; i < iTempAry3.length; i++)
            iTempAry3[i] = iTempAry2[i];

        return iTempAry3;
    }

    public static void main(String args[])
    {
        Scanner scan = new Scanner(System.in);

        // Enter the size of iAry1
        System.out.print("Enter the size of Array1 >> ");
        int length1 = scan.nextInt();

        int[] iAry1 = new int[length1];

        // Enter the elements of iAry1
        System.out.print("Enter ");
        System.out.print(length1 + " elements of Array1 >> ");
        for (int i = 0; i < iAry1.length; i++)
            iAry1[i] = scan.nextInt();

        // Enter the size of iAry2
        System.out.print("Enter the size of Array1 >> ");
        int length2 = scan.nextInt();

        int[] iAry2 = new int[length2];

        // Enter the elements of iAry2
        System.out.print("Enter ");
        System.out.print(length2 + " elements of Array2 >> ");
        for (int i = 0; i < iAry2.length; i++)
            iAry2[i] = scan.nextInt();

        // 'tempAry1' = 'iAry1' + 'iAry2'
        int[] tempAry1 = concat(iAry1, iAry2);

        // 'tempAry2' = 'iAry1' - 'iAry2'
        int[] tempAry2 = remove(iAry1, iAry2);

        // Print 'tempAry1'
        System.out.print("Array1 + Array2 = { ");
        for (int num : tempAry1)

            System.out.print(num + " ");
        System.out.println("}");

        // Print 'tempAry2'
        System.out.print("Array1 - Array2 = { ");
        for (int num : tempAry2)

            System.out.print(num + " ");
        System.out.println("}");

    }
}
