/**
 * @date : 2017. 5. 25.
 */
/**
 * <pre>
 *  
 *    |_ Ex05.java
 * 
 * </pre>
 * @date : 2017. 5. 25. ���� 10:44:25
 * @version : 
 * @author : Jho
 */

import java.util.*;

class Student {
    String name;
    String department;
    int id;
    double gradesAverage;

    Student() {
        name = null;
        department = null;
        id = -1;
        gradesAverage = -1;
    }

    Student(String name, String department, int id, double gradesAverage) {
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

public class Ex05 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        ArrayList<Student> myClass = new ArrayList<Student>();

        // Input
        for (int i = 0; i < 5; i++) {
            System.out.print((i + 1) + "��° �л��� �̸� >> ");
            String name = scan.next();
            System.out.print((i + 1) + "��° �л��� �а� >> ");
            String department = scan.next();
            System.out.print((i + 1) + "��° �л��� �й� >> ");
            int id = scan.nextInt();
            System.out.print((i + 1) + "��° �л��� ���� ��� >> ");
            double gradesAverage = scan.nextDouble();

            Student tmp = new Student(name, department, id, gradesAverage);
            myClass.add(tmp);

        }

        Iterator<Student> it = myClass.iterator();

        while (it.hasNext()) {
            it.next().showInfo();
        }
    }

}