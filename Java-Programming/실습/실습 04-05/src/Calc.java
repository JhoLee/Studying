/**
 * @date : 2017. 4. 4.
 */
/**
 * <pre>
 *   (default package)
 *    |_ Calc.java
 * </pre>
 * 
 * @date : 2017. 4. 4. 오후 2:42:34
 * @version :
 * @author : Jho
 */

// This file includes the 'main method'.
import java.util.Scanner;

class Add
{

    private int a;

    private int b;

    public void setValue(int a, int b)
    {
        this.a = a;
        this.b = b;
    }

    public int calculate()
    {
        return (a + b);
    }
}

class Sub
{

    private int a;

    private int b;

    public void setValue(int a, int b)
    {
        this.a = a;
        this.b = b;
    }

    public int calculate()
    {
        return (a - b);
    }
}

class Mul
{

    private int a;

    private int b;

    public void setValue(int a, int b)
    {
        this.a = a;
        this.b = b;
    }

    public int calculate()
    {
        return (a * b);
    }
}

class Div
{

    private int a;

    private int b;

    public void setValue(int a, int b)
    {
        this.a = a;
        this.b = b;
    }

    public int calculate()
    {
        if (b == 0)
            return -295;
        else
            return (a / b);
    }
}

// This class includes 'main method'
public class Calc
{

    public static int iCalc(int x, int y, char op)
    {
        switch (op)
        {
            case '+':
                Add add = new Add();
                add.setValue(x, y);
                return add.calculate();
            case '-':
                Sub sub = new Sub();
                sub.setValue(x, y);
                return sub.calculate();
            case '*':
                Mul mul = new Mul();
                mul.setValue(x, y);
                return mul.calculate();
            case '/':
                Div div = new Div();
                div.setValue(x, y);
                return div.calculate();
            default:
                return -295;
        }
    }

    public static void main(String args[])
    {
        int result = 0;
        while (true)
        {
            Scanner scan = new Scanner(System.in);
            System.out.println("두 정수와 연산자를 입력하시오(postfix)");
            System.out.print("Ex)\"3+4\" -> \"3 4 +\" >> ");
            int x = scan.nextInt();
            int y = scan.nextInt();
            char op = scan.next().charAt(0);
            // Calculation
            result = iCalc(x, y, op);
            if (result == -295)
                System.out.println("Input ERROR");
            else
                System.out.println(result);
            System.out.println();
        }
    }
}
