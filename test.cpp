#include <iostream>
#include <deque>
using namespace std;

int main() {

	deque <int> dq;
    int N, M;
    int answer = 0;

	cin >> N >> M;

	for (int i = 1; i <= N; i++)
		dq.push_back(i);

	int num;
	while (M--) {
		cin >> num;

		int idx_front = -1;
		for (int i = 0; i < dq.size(); i++) {
			if (num == dq[i])
				idx_front = i;
		}

		int idx_back = dq.size() - idx_front;

		if (idx_front <= idx_back) {
			for (int i = 0; i < idx_front; i++) {
				int temp = dq.front();
				dq.push_back(temp);
				dq.pop_front();
			}
			dq.pop_front();
			answer += idx_front;
		}
		else {
			for (int i = dq.size() - 1; i >= idx_front; i--) {
				int temp = dq.back();
				dq.push_front(temp);
				dq.pop_back();
			}
			dq.pop_front();
			answer += idx_back;
		}
	}
	cout << answer;
}





