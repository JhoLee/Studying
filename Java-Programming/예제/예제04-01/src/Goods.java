/**
 * @date : 2017. 4. 17.
 */
/**
 * <pre>
 *  
 *    |_ Goods.java
 * </pre>
 * 
 * @date : 2017. 4. 17. ���� 10:37:44
 * @version :
 * @author : Jho
 */

public class Goods {
    String name;
    int price;
    int numberOfStock;
    int sold;

    public static void main(String args[]) {
	Goods camera = new Goods();
	camera.name = "Nikon";
	camera.price = 4000000;
	camera.numberOfStock = 30;
	camera.sold = 50;
	System.out.println("��ǰ �̸�: " + camera.name);
	System.out.println("��ǰ ����: " + camera.price);
	System.out.println("��� ����: " + camera.numberOfStock);
	System.out.println("�ȸ� ����: " + camera.sold);
    }
}