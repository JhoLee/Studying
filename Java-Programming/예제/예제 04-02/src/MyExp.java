/**
 * @date : 2017. 4. 17.
 */
/**
 * <pre>
 *  
 *    |_ MyExp.java
 * 
 * </pre>
 * 
 * @date : 2017. 4. 17. ¿ÀÈÄ 10:53:35
 * @version :
 * @author : Jho
 */
public class MyExp {
    int base;
    int exp;

    int getValue() {
	int res = 1;
	for (int i = 0; i < exp; i++)
	    res *= base;
	return res;
    }

    public static void main(String[] args) {
	MyExp number1 = new MyExp();
	number1.base = 2;
	number1.exp = 3;
	MyExp number2 = new MyExp();
	number2.base = 3;
	number2.exp = 4;

	System.out.println(number1.base + "ÀÇ " + number1.exp + "½Â = "
		+ number1.getValue());
	System.out.println(number2.base + "ÀÇ " + number2.exp + "½Â = "
		+ number2.getValue());
    }

}
