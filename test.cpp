#include <iostream>
using namespace std;

int main() {

	int N, M;
	cin >> N >> M;

	int before = 0;
	int node = 1;
	for (int i = 0; i < N-M; i++) {
		cout << before << ' ' << node << endl;
		before = node++;
	}
	
	for (int i = 0; i < M-1; i++) {
		cout << before << ' ' << node ++<< endl;
	}

	return 0;
}


