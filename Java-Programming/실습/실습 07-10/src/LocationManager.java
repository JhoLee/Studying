/**
 * @date : 2017. 5. 26.
 */
/**
 * <pre>
 *  
 *    |_ LocationManager.java
 * 
 * </pre>
 * @date : 2017. 5. 26. 오전 9:28:42
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
        System.out.println("지명 : " + name);
        System.out.println("(위도, 경도) : (" + lattitude + ", " + longitude + ")");
        System.out.println();
    }

}

public class LocationManager {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        HashMap<String, Location> location = new HashMap<String, Location>();

        // input
        for (int i = 0; i < 5; i++) {
            System.out.print("지명을 입력 >> ");
            String name = scan.next();
            System.out.print("위도, 경도를 입력 >> ");
            double lattitude = scan.nextDouble();
            double longitude = scan.nextDouble();

            location.put(name, new Location(name, lattitude, longitude));
        }

        // search
        while (true) {
            System.out.print("검색할 지명을 입력 >> ");
            String key = scan.next();
            try {
                location.get(key).showInfo();
            } catch (Exception e) {
                System.out.println("\'" + key + "\'에 해당하는 데이터가 없습니다.");
            }
        }
    }

}
