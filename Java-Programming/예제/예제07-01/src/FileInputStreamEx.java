/**
 * @date : 2017. 6. 19.
 */
/**
 * <pre>
 *  
 *    |_ FileInputStreamEx.java
 * 
 * </pre>
 * @date : 2017. 6. 19. 오전 12:52:51
 * @version : 
 * @author : Jho
 */

import java.io.*;

public class FileInputStreamEx {
    public static void main(String[] args) {

        FileOutputStream fout = null;
        try {
            fout = new FileOutputStream("e:\\test.txt");
            int num[] = { 1, 4, -1, 88, 50 };
            byte b[] = { 7, 51, 3, 4, 1, 24 };
            for (int i = 0; i < num.length; i++)
                fout.write(num[i]);
            fout.write(b);
            fout.close();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        
        FileInputStream in = null;
        try {
            in = new FileInputStream("e:\\test.txt");

            int c;
            while ((c = in.read()) != -1) {
                System.out.print((char) c);
            }
            in.close();

        } catch (IOException e) {
            System.out.println("입출력 오류");
        }

    }

}
