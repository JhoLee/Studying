
/**
 * <pre>
 *  (default package)
 *    |_ GoodsArray.java
 * </pre>
 * 
 * @date : 2017. 3. 30. 오후 11:05:04
 * @version :
 * @author : Jho
 */
import java.util.Scanner;

public class GoodsArray
{
    public static void main(String args[])
    {
        Goods[] goodsArray; // 배열 선언
        goodsArray = new Goods[3]; // Goods 객체 레퍼런스 배열 생성

        Scanner s = new Scanner(System.in);
        for (int i = 0; i < goodsArray.length; i++)
        {
            String name = s.next(); // 상품 이름
            int price = s.nextInt();// 상품 가격
            int n = s.nextInt(); // 상품 재고
            int sold = s.nextInt(); // 팔린 수량
            goodsArray[i] = new Goods(name, price, n, sold); // Goods 객체 생성
        }

        for (int i = 0; i < goodsArray.length; i++)
        {
            System.out.print(goodsArray[i].getName() + " "); // 상품 이름 출력
            System.out.print(goodsArray[i].getPrice() + " "); // 상품 가격 출력
            System.out.print(goodsArray[i].getNumberOfStock() + " "); // 상품 재고
                                                                      // 출력
            System.out.println(goodsArray[i].getSold()); // 팔린 수량 출력
        }
    }
}

class Goods
{
    private String name;
    private int price;
    private int numberOfStock;
    private int sold;

    Goods(String n, int p, int nStock, int s) // 생성자
    {
        name = n;
        price = p;
        numberOfStock = nStock;
        sold = s;
    }

    String getName()
    {
        return name;
    } // 상품 이름 리턴

    int getPrice()
    {
        return price;
    } // 상품 가격 리턴

    int getNumberOfStock()
    {
        return numberOfStock;
    } // 상품 재고 리턴

    int getSold()
    {
        return sold;
    } // 팔린 수량 리턴
}
