/**
 * @date : 2017. 5. 26.
 */
/**
 * <pre>
 *  
 *    |_ Ex09.java
 * 
 * </pre>
 * @date : 2017. 5. 26. ���� 9:10:58
 * @version : 
 * @author : Jho
 */

import java.util.*;

public class Ex09 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        HashMap<String, Student> dept = new HashMap<String, Student>();

        // Input
        for (int i = 0; i < 5; i++) {
            System.out.print((i + 1) + "��° �л��� �̸� >> ");
            String name = scan.next();
            System.out.print((i + 1) + "��° �л��� �а� >> ");
            String department = scan.next();
            System.out.print((i + 1) + "��° �л��� �й� >> ");
            String id = scan.next();
            System.out.print((i + 1) + "��° �л��� ���� ��� >> ");
            double gradesAverage = scan.nextDouble();

            Student tmp = new Student(name, department, id, gradesAverage);
            dept.put(id, tmp);

        }

        // Search
        while (true) {
            System.out.println("ã���� �ϴ� �л��� �й� >> ");
            String searchID = scan.next();
            try {
                dept.get(searchID).showInfo();
            } catch (Exception e) {
                System.out.println("���� �й��Դϴ�.");
            }
        }

    }
}

class Student {
    String name;
    String department;
    String id;
    double gradesAverage;

    Student() {
        name = null;
        department = null;
        id = null;
        gradesAverage = -1;
    }

    Student(String name, String department, String id, double gradesAverage) {
        this.name = name;
        this.department = department;
        this.id = id;
        this.gradesAverage = gradesAverage;
    }

    void showInfo() {
        System.out.println("�̸� : " + name);
        System.out.println("�а� : " + department);
        System.out.println("�й� : " + id);
        System.out.println("���� ��� : " + gradesAverage);
        System.out.println();
    }
}
