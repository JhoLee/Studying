import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);

		// 스택 배열 생성
		System.out.println("생성할 스택 메모리의 수를 입력하시오 >> ");
		int num = scan.nextInt();
		Stack[] stackArray = new Stack[num];

		// 메뉴
		for (int i = 1; i <= stackArray.length; i++) {

			System.out.print("(" + i + ")번 스택 ");
			if (i % 3 == 0)
				System.out.println();
		}
		System.out.println("접근할 스택의 번호를 입력 >> ");
		int n = scan.nextInt();

		// n번 스택 접근

	}
 
}
