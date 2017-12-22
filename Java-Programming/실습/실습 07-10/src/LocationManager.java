/**
 * @date : 2017. 5. 26.
 */
/**
 * <pre>
 *  
 *    |_ LocationManager.java
 * 
 * </pre>
 * @date : 2017. 5. 26. ���� 9:28:42
 * @version : 
 * @author : Jho
 */

import java.util.*;

class Location {
    String name;
    double lattitude;
    double longitude;

    public Location() {
        name = null;
        lattitude = -1;
        longitude = -1;
    }

    public Location(String name, double lattitude, double longitude) {
        this.name = name;
        this.lattitude = lattitude;
        this.longitude = longitude;
    }

    public void showInfo() {
        System.out.println("���� : " + name);
        System.out.println("(����, �浵) : (" + lattitude + ", " + longitude + ")");
        System.out.println();
    }

}

public class LocationManager {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        HashMap<String, Location> location = new HashMap<String, Location>();

        // input
        for (int i = 0; i < 5; i++) {
            System.out.print("������ �Է� >> ");
            String name = scan.next();
            System.out.print("����, �浵�� �Է� >> ");
            double lattitude = scan.nextDouble();
            double longitude = scan.nextDouble();

            location.put(name, new Location(name, lattitude, longitude));
        }

        // search
        while (true) {
            System.out.print("�˻��� ������ �Է� >> ");
            String key = scan.next();
            try {
                location.get(key).showInfo();
            } catch (Exception e) {
                System.out.println("\'" + key + "\'�� �ش��ϴ� �����Ͱ� �����ϴ�.");
            }
        }
    }

}
