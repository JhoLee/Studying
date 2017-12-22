#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;


int main() {

	ifstream fin;
	fin.open("input.txt");

	ofstream fout;
	fout.open("output.txt");

	int N; // Number of Students



	try {


		while (fin >> N) {

			fout << "Simulation : " << endl;

			char *locker = new char[N + 1];

			for (int i = 1; i <= N; i++) {
				locker[i] = 'X';
			}

			for (int i = 1; i <= N; i++) {
				fout << i << "번째 학생 등교 : ";

				for (int j = 1; j <= N; j++) {
					if (j % i == 0) {
						if (locker[j] == 'O') {
							locker[j] = 'X';
						}
						else {
							locker[j] = 'O';
						}
					}
					fout << locker[j];

				}
				fout << endl;
			}

			fout << "Solution(열려있는 사물함 번호) : " << endl;
			for (int i = 1; i <= N; i++) {
				if (locker[i] == 'O') {
					fout << setw(4) << i;
				}
			}
			fout << endl;

		}
		fout << endl;

	}
	catch (exception e) {
		cout << "ERROR";

	}

	fin.close();
	fout.close();

	return 0;
}