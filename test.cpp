#include <iostream>
#include <string>

using namespace std;

int main() {
    int N, M, p, s;
    cin >> N >> M;

    int package = 1000, single = 1000;

    for (int i = 0; i < M; i++) {
        cin >> p >> s;
        package = min(package, p);
        single = min(single, s);
    }

    int price = min((N / 6 + 1) * package,
                    min(N / 6 * package + N % 6 * single, N * single));

    cout << price;

    return 0;
}



