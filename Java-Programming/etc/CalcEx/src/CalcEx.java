/**
 * @date : 2017. 4. 3.
 */
/**
 * <pre>
 *  
 *    |_ CalcEx.java
 * 
 * </pre>
 * @date : 2017. 4. 3. ¿ÀÈÄ 5:45:53
 * @version : 
 * @author : Jho
 */


public class CalcEx
{
    public static void main(String[] args)
    {
        Calc a = new Calc();
        a.setValue(30, 12);
        System.out.println(a.add());

        Calc b = new Calc(1.56, 3.4);
        System.out.println(b.div());
    }
}
