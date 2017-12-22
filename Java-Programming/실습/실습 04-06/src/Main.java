/*
 */
/**
 * <pre>
 *  
 *    |_ Main.java
 * 
 * </pre>
 * 
 * @date : 2017. 4. 5. 오후 3:38:00
 * @version :
 * @author : Jho
 */

import java.util.Scanner;

public class Main
{

    public static void main(String args[])
    {
        Scanner scan = new Scanner(System.in);
        // Creating object array of sSeat...
        Seat[] sSeat = Seat.createSeats(10, 'S');
        // Creating object array of sSeat...
        Seat[] aSeat = Seat.createSeats(10, 'A');
        // Creating object array of sSeat...
        Seat[] bSeat = Seat.createSeats(10, 'B');
        // Main Menu
        int op = 4;
        do
        {
            System.out.print("예약<1>, 조회<2>, 취소<3>, 끝내기<4> >> ");
            op = scan.nextInt();
            switch (op)
            {
                // 예약
                case 1:
                    System.out.print("좌석구분 S<1>, A<2>, B<3> >> ");
                    switch (scan.nextInt())
                    {
                        case 1:
                            Menu.reservation(sSeat);
                            break;
                        case 2:
                            Menu.reservation(aSeat);
                            break;
                        case 3:
                            Menu.reservation(bSeat);
                            break;
                        default:
                            System.out.println("잘못된 입력입니다.");
                            break;
                    }
                    break;
                // 조회
                case 2:
                    Menu.lookUp(sSeat);
                    Menu.lookUp(aSeat);
                    Menu.lookUp(bSeat);
                    System.out.println("<<<조회를 완료하였습니다.>>>");
                    break;
                // 취소
                case 3:
                    System.out.print("좌석구분 S<1>, A<2>, B<3> >> ");
                    switch (scan.nextInt())
                    {
                        case 1:
                            Menu.Cancel(sSeat);
                            break;
                        case 2:
                            Menu.Cancel(aSeat);
                            break;
                        case 3:
                            Menu.Cancel(bSeat);
                            break;
                        default:
                            System.out.println("잘못된 입력입니다.");
                            break;
                    }
                    break;
                // 끝내기
                case 4:
                    System.out.println("<<프로그램을 종료합니다.>>");
                    break;
                default:
                    System.out.println("잘못된 입력입니다.");
            }
        } while (op != 4);
    }
}

// 좌석
class Seat
{

    // 해당 좌석의 예약자명
    private String name;

    // 해당 좌석의 등급
    private char grade;

    public Seat(char grade)
    {
        name = getEmptySeat();
        this.grade = grade;
    }

    // 공석에 해당하는 문자열 조회
    public String getEmptySeat()
    {
        return "---";
    }

    // 예약자명 등록
    public void setName(String name)
    {
        this.name = name;
    }

    // 예약자명 해제
    public void deleteName()
    {
        this.name = getEmptySeat();
    }

    // 예약자명 조회
    public String getName()
    {
        return name;
    }

    public char getGrade() // 좌석등급 조회
    {
        return grade;
    }

    // 'num'개의 'grade'등급 좌석 배열 return
    public static Seat[] createSeats(int num, char grade)
    {
        Seat[] tempSeat = new Seat[num + 1];
        for (int i = 0; i < tempSeat.length; i++)
        {
            tempSeat[i] = new Seat(grade);
        }
        return tempSeat;
    }
}

class Menu
{

    /**
     * @목적 : 좌석 예약
     * @절차
     *     1) 좌석등급 입력 </br>
     *     2) 해당 등급의 좌석들 예약 현황 출력 </br>
     *     3) 예약자명 입력 </br>
     *     4) 예약할 좌석 번호 입력 </br>
     *     4-1) 해당 좌석이 공석 -> 예약 </br>
     *     4-2) else -> 오류 출력 </br>
     * 
     */
    public static void reservation(Seat[] seat)
    {
        Scanner scan = new Scanner(System.in);
        Menu.lookUp(seat);
        System.out.print("이름>> ");
        String name = scan.next();
        System.out.print("번호>> ");
        int num = scan.nextInt();
        if (seat[num].getName() == seat[num].getEmptySeat())
            seat[num].setName(name);
        else
            System.out.println("해당 좌석은 이미 예약되어 있습니다.");
    }

    /**
     * @목적 : 좌석 예약 취소
     * @절차
     *     1) 좌석등급 입력 </br>
     *     2) 해당 등급의 좌석들 예약 현황 출력 </br>
     *     3) 취소할 예약자명 입력 </br>
     *     3-1) 해당 예약자가 존재 -> 해당 예약자 예약 취소 & return true</br>
     *     3-2) else -> 오류 출력 & return false</br>
     * 
     */
    public static void Cancel(Seat[] seat)
    {
        Scanner scan = new Scanner(System.in);
        Menu.lookUp(seat);
        System.out.print("이름>> ");
        String name = scan.next();
        int count = 0;
        for (int i = 1; i < seat.length; i++)
        {
            if (seat[i].getName().matches(name))
            {
                seat[i].deleteName();
                count += 1;
            }
        }
        if (count == 0)
            System.out.println("해당하는 예약자가 없습니다.");
        else
            System.out.println("<<예약 취소 성공!>>");
    }

    /**
     * @목적 : 좌석 예약 현황 출력
     * @절차
     *     1) 좌석등급 입력 </br>
     *     2) 좌석 등급명 출력 </br>
     *     3) 해당 등급의 좌석 예약 현황 출력 </br>
     * 
     */
    public static void lookUp(Seat[] seat)
    {
        System.out.print(seat[1].getGrade() + ">>");
        for (int i = 1; i < seat.length; i++)
        {
            System.out.print(" " + seat[i].getName());
        }
        System.out.println();
    }
}
