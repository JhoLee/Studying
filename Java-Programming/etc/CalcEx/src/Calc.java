/**
 * @date : 2017. 4. 3.
 */
/**
 * <pre>
 *   (default package)
 *    |_ Calc.java
 * </pre>
 * 
 * @date : 2017. 4. 3. ¿ÀÈÄ 5:25:13
 * @version :
 * @author : Jho
 */
public class Calc
{
    private double x;
    private double y;

    public Calc()
    {
        x = y = 0.0;
    }

  

    public Calc(double x, double y)
    {
        this.x = x;
        this.y = y;
    }

   
    public double add()
    {
        return x + y;
    }

    public double sub()
    {
        return x - y;
    }

    public double div()
    {

        try
        {
            return x / y;
        } catch (Exception e)
        {
            System.out.println("ERROR");
        }
        return -1.0;

    }

    public double mul()
    {
        return x * y;
    }

    public void setValue(double x, double y)
    {
        this.x = x;
        this.y = y;
    }

    public double getX()
    {
        return this.x;
    }

    public double getY()
    {
        return this.y;
    }

}