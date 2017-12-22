/**
 * @date : 2017. 5. 25.
 */
/**
 * <pre>
 *  
 *    |_ GradeEx.java
 * 
 * </pre>
 * @date : 2017. 5. 25. ¿ÀÈÄ 2:09:16
 * @version : 
 * @author : Jho
 */

import java.io.*;

public class GradeEx {
    public static void main(String args[]) {

        BufferedReader in = null;
        try {

            in = new BufferedReader(new FileReader("E:\\grade.txt"));

            String str;

            while ((str = in.readLine()) != null) {
                String[] data = str.trim().split(" ");
                String name = data[0];
                int kor = Integer.parseInt(data[1]);
                int eng = Integer.parseInt(data[2]);
                int mat = Integer.parseInt(data[3]);
                int total = kor + eng + mat;
                double mean = total / 3.0;

                System.out.println(name + ": " + mean);
            }
        } catch (IOException e) {
            System.out.println("IO Error");
        }
    }

}
