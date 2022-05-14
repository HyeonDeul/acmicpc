#include <iostream>
#include <string>

using namespace std;

const int MAX = 1e5;

class Deque{
    private :
        int data[MAX];
        int idx_front;
        int idx_back;

    public :
        Deque(){
            idx_front = 0;
            idx_back = 0;
        }
        void push_front(int x){
            data[idx_front] = x;
            idx_front = (idx_front - 1 + MAX) % MAX;
        }
        void push_back(int x){
            idx_back = (idx_back + 1) % MAX;
            data[idx_back] = x;
        }
        void pop_front(){
            idx_front = (idx_front +1)% MAX;
        }
        void pop_back(){
            idx_back = (idx_back-1+MAX)% MAX;
        }
        int front(){
            return data[(idx_front + 1) % MAX];
        }
        int back(){
            return data[idx_back];
        }
        int size(){
            return (idx_back - idx_front) % MAX;
        }
};

int main() {


    return 0;
}



