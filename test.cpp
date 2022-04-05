#include <algorithm>
#include <iostream>
#include <string>
using namespace std;

int main() {
    string hansoo;  // 한수 영어 이름
    cin >> hansoo;  // 입력받기
    string fdr;     // 한수 영어 이름 길이만큼 팰린드롬 할당
    fdr.resize(100);
    sort(hansoo.begin(), hansoo.end());  // 오름차순 정리

    int front = 0, behind = hansoo.size();  // 팰린드롬 인덱스
    char word = hansoo[0];
    int count = 1,
        count_ =
            0;  // count -> 홀짝 구분용 / count_ -> 홀수일 때 가운데 구분 용
    for (int i = 1; i <= hansoo.size(); i++) {
        if (word == hansoo[i]) {  // 앞 단어와 다음 단어가 같으면 count 증가 ->
                                  // count가 홀수일 때 / 짝수일 때 나뉨
            count++;
        } else {
            if (count % 2 == 1) {  // 한 단어라도 홀수개 있는 단어 존재
                if (hansoo.size() % 2 == 0) {  // 이름의 길이 짝수일 때
                    cout << "I'm Sorry Hansoo";
                    return 0;
                }
                if (count_ == 0) {
                    fdr[hansoo.size() / 2 + 1] =
                        word;  // 단어 갯수가 홀수일 때 가운데에 한 개 들어가는
                               // 용
                    for (int j = 0; j < count / 2; j++) {
                        fdr[front] = word;
                        fdr[behind] = word;
                        behind--;
                        front++;
                    }
                    count_ = 1;  // 홀수개인 단어가 2개 이상이면 안됨.
                } else {         // 홀수개인 단어가 여러개면 안됨
                    cout << "I'm Sorry Hansoo";
                    return 0;
                }
            } else {
                for (int q = 0; q < count / 2; q++) {
                    fdr[front] = word;
                    fdr[behind] = word;
                    front++;
                    behind--;
                }
            }
            word = hansoo[i];  // 다음 단어로 넘어가기
            count = 1;         // 다시 1 로 초기화
        }
    }

    cout << fdr;

    return 0;
}