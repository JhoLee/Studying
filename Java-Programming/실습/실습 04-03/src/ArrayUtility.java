/**
 * @date : 2017. 4. 3.
 */
/**
 * <pre>
 *  
 *    |_ ArrayUtility.java
 * </pre>
 * 
 * @date : 2017. 4. 3. ¿ÀÈÄ 8:43:40
 * @version :
 * @author : Jho
 */
public class ArrayUtility
{
    
    static int[] doubleToInt(double[] source)
    {
        int iTemp[] = new int[source.length];
        for (int i=0; i<source.length; i++)
            iTemp[i] = source[i];
        return iTemp;
        
    }

    static double[] intToDouble(int[] source)
    {
        double dTemp[] = new double[source.length];
        for (int i = 0; i < source.length; i++)
            dTemp[i] = source[i];
        return dTemp;
    }

    double [] intToDouble()

}
