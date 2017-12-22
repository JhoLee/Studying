import java.util.*;

public class A {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// Number of test cases
		int T = sc.nextInt();

		for (int i = 0; i < T; i++) {

			// Data Input
			int H = sc.nextInt(); // Number of floors
			int W = sc.nextInt(); // Number of rooms in single floor
			int N = sc.nextInt(); // The order of guest

			// Computing..
			int height = N % H;
			int weight = 1 + (N / H);
			
			// room
			int room = height*100 + weight;

			// Printing..
			System.out.println(room);

		}
		
		

	}

}
