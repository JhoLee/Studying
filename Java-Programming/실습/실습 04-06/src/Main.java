/*
 */
/**
 * <pre>
 *  
 *    |_ Main.java
 * 
 * </pre>
 * 
 * @date : 2017. 4. 5. ���� 3:38:00
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
            System.out.print("����<1>, ��ȸ<2>, ���<3>, ������<4> >> ");
            op = scan.nextInt();
            switch (op)
            {
                // ����
                case 1:
                    System.out.print("�¼����� S<1>, A<2>, B<3> >> ");
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
                            System.out.println("�߸��� �Է��Դϴ�.");
                            break;
                    }
                    break;
                // ��ȸ
                case 2:
                    Menu.lookUp(sSeat);
                    Menu.lookUp(aSeat);
                    Menu.lookUp(bSeat);
                    System.out.println("<<<��ȸ�� �Ϸ��Ͽ����ϴ�.>>>");
                    break;
                // ���
                case 3:
                    System.out.print("�¼����� S<1>, A<2>, B<3> >> ");
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
                            System.out.println("�߸��� �Է��Դϴ�.");
                            break;
                    }
                    break;
                // ������
                case 4:
                    System.out.println("<<���α׷��� �����մϴ�.>>");
                    break;
                default:
                    System.out.println("�߸��� �Է��Դϴ�.");
            }
        } while (op != 4);
    }
}

// �¼�
class Seat
{

    // �ش� �¼��� �����ڸ�
    private String name;

    // �ش� �¼��� ���
    private char grade;

    public Seat(char grade)
    {
        name = getEmptySeat();
        this.grade = grade;
    }

    // ������ �ش��ϴ� ���ڿ� ��ȸ
    public String getEmptySeat()
    {
        return "---";
    }

    // �����ڸ� ���
    public void setName(String name)
    {
        this.name = name;
    }

    // �����ڸ� ����
    public void deleteName()
    {
        this.name = getEmptySeat();
    }

    // �����ڸ� ��ȸ
    public String getName()
    {
        return name;
    }

    public char getGrade() // �¼���� ��ȸ
    {
        return grade;
    }

    // 'num'���� 'grade'��� �¼� �迭 return
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
     * @���� : �¼� ����
     * @����
     *     1) �¼���� �Է� </br>
     *     2) �ش� ����� �¼��� ���� ��Ȳ ��� </br>
     *     3) �����ڸ� �Է� </br>
     *     4) ������ �¼� ��ȣ �Է� </br>
     *     4-1) �ش� �¼��� ���� -> ���� </br>
     *     4-2) else -> ���� ��� </br>
     * 
     */
    public static void reservation(Seat[] seat)
    {
        Scanner scan = new Scanner(System.in);
        Menu.lookUp(seat);
        System.out.print("�̸�>> ");
        String name = scan.next();
        System.out.print("��ȣ>> ");
        int num = scan.nextInt();
        if (seat[num].getName() == seat[num].getEmptySeat())
            seat[num].setName(name);
        else
            System.out.println("�ش� �¼��� �̹� ����Ǿ� �ֽ��ϴ�.");
    }

    /**
     * @���� : �¼� ���� ���
     * @����
     *     1) �¼���� �Է� </br>
     *     2) �ش� ����� �¼��� ���� ��Ȳ ��� </br>
     *     3) ����� �����ڸ� �Է� </br>
     *     3-1) �ش� �����ڰ� ���� -> �ش� ������ ���� ��� & return true</br>
     *     3-2) else -> ���� ��� & return false</br>
     * 
     */
    public static void Cancel(Seat[] seat)
    {
        Scanner scan = new Scanner(System.in);
        Menu.lookUp(seat);
        System.out.print("�̸�>> ");
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
            System.out.println("�ش��ϴ� �����ڰ� �����ϴ�.");
        else
            System.out.println("<<���� ��� ����!>>");
    }

    /**
     * @���� : �¼� ���� ��Ȳ ���
     * @����
     *     1) �¼���� �Է� </br>
     *     2) �¼� ��޸� ��� </br>
     *     3) �ش� ����� �¼� ���� ��Ȳ ��� </br>
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
