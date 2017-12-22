public class Stack {
	private int[] data;
	private int stackPoint;

	public Stack(int size) {
		data = new int[size];
		for (int i = 0; i < data.length; i++) {
			data[i] = 0;
		}
		stackPoint = 0;
	}

	public void push(int element) {
		if (isFull() == true)
			System.out.println("OverFlow");
		else {
			data[stackPoint++] = element;
			System.out.println(element + "was successfully pushed.");
		}

	}

	public int pop() {
		if (isEmpty() == true) {
			System.out.println("OverFlow");
			return -1;
		} else
			return data[stackPoint--];
	}

	public boolean isEmpty() {
		if (stackPoint <= 0)
			return true;
		else
			return false;
	}

	public boolean isFull() {
		if (stackPoint >= data.length)
			return true;
		else
			return false;
	}

	public void reset() {
		stackPoint = 0;
		System.out.println("The stack was reset.");
	}

}