#include <iostream>
#include <string>
#include <fstream>
using namespace std;


int main() {

	int h, y, d, m, k, j;

	ifstream fin;
	fin.open("input.txt");

	ofstream fout;
	fout.open("output.txt");

	try {
		while (fin >> y >> m >> d) {

			if (m == 1 || m == 2) {
				m += 12;
				y -= 1;
			}

			j = y / 100;
			k = y % 100;

			h = (d + (int)((m + 1) * 26 / 10) + k + (k / 4) + (j / 4) + (j * 5)) % 7;




			switch (h) {
			case 0:
				fout << "요일은 토요일입니다." << endl;
				break;

			case 1:
				fout << "요일은 일요일입니다." << endl;
				break;

			case 2:
				fout << "요일은 월요일입니다." << endl;
				break;

			case 3:
				fout << "요일은 화요일입니다." << endl;
				break;

			case 4:
				fout << "요일은 수요일입니다." << endl;
				break;

			case 5:
				fout << "요일은 목요일입니다." << endl;
				break;

			case 6:
				fout << "요일은 금요일입니다." << endl;
				break;

			}






		}
	}
	catch (exception e) {

	}

	fin.close();
	fout.close();

	return 0;
}