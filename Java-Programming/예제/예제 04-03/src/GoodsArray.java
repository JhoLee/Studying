
/**
 * <pre>
 *  (default package)
 *    |_ GoodsArray.java
 * </pre>
 * 
 * @date : 2017. 3. 30. ���� 11:05:04
 * @version :
 * @author : Jho
 */
import java.util.Scanner;

public class GoodsArray
{
    public static void main(String args[])
    {
        Goods[] goodsArray; // �迭 ����
        goodsArray = new Goods[3]; // Goods ��ü ���۷��� �迭 ����

        Scanner s = new Scanner(System.in);
        for (int i = 0; i < goodsArray.length; i++)
        {
            String name = s.next(); // ��ǰ �̸�
            int price = s.nextInt();// ��ǰ ����
            int n = s.nextInt(); // ��ǰ ���
            int sold = s.nextInt(); // �ȸ� ����
            goodsArray[i] = new Goods(name, price, n, sold); // Goods ��ü ����
        }

        for (int i = 0; i < goodsArray.length; i++)
        {
            System.out.print(goodsArray[i].getName() + " "); // ��ǰ �̸� ���
            System.out.print(goodsArray[i].getPrice() + " "); // ��ǰ ���� ���
            System.out.print(goodsArray[i].getNumberOfStock() + " "); // ��ǰ ���
                                                                      // ���
            System.out.println(goodsArray[i].getSold()); // �ȸ� ���� ���
        }
    }
}

class Goods
{
    private String name;
    private int price;
    private int numberOfStock;
    private int sold;

    Goods(String n, int p, int nStock, int s) // ������
    {
        name = n;
        price = p;
        numberOfStock = nStock;
        sold = s;
    }

    String getName()
    {
        return name;
    } // ��ǰ �̸� ����

    int getPrice()
    {
        return price;
    } // ��ǰ ���� ����

    int getNumberOfStock()
    {
        return numberOfStock;
    } // ��ǰ ��� ����

    int getSold()
    {
        return sold;
    } // �ȸ� ���� ����
}
