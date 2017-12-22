/**
 * @date : 2017. 5. 26.
 */
/**
 * <pre>
 *  
 *    |_ Ex09.java
 * 
 * </pre>
 * @date : 2017. 5. 26. 오전 9:10:58
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
            System.out.print((i + 1) + "번째 학생의 이름 >> ");
            String name = scan.next();
            System.out.print((i + 1) + "번째 학생의 학과 >> ");
            String department = scan.next();
            System.out.print((i + 1) + "번째 학생의 학번 >> ");
            String id = scan.next();
            System.out.print((i + 1) + "번째 학생의 학점 평균 >> ");
            double gradesAverage = scan.nextDouble();

            Student tmp = new Student(name, department, id, gradesAverage);
            dept.put(id, tmp);

        }

        // Search
        while (true) {
            System.out.println("찾고자 하는 학생의 학번 >> ");
            String searchID = scan.next();
            try {
                dept.get(searchID).showInfo();
            } catch (Exception e) {
                System.out.println("없는 학번입니다.");
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
        System.out.println("이름 : " + name);
        System.out.println("학과 : " + department);
        System.out.println("학번 : " + id);
        System.out.println("학점 평균 : " + gradesAverage);
        System.out.println();
    }
}
