#include <iostream>
#include <string>
using namespace std;

int main()
{

    int N;
    cin >> N;

    string standard;
    cin >> standard;
    int l = standard.length();

    string temp;
    for (int i = 1; i < N; i++)
    {
        cin >> temp;
        for (int j = 0; j < l; j++)
        {
            if (standard[j] != temp[j])
            {
                standard[j] = '?';
            }
        }
    }

    cout << standard << '\n';
    return 0;
}
