import sys
N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

front = 0
back = N-1

s = sum(arr)
if s > S:
    while front != back:
        if arr[front] < arr[back]:
            s -= arr[front]
            if s < S:
                break
            front += 1
        else:
            s -= arr[back]
            if s < S:
                break
            back -= 1

    print(back-front+1)
print(0)
