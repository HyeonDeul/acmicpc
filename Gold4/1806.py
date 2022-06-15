import sys
N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

front = 0
back = 0

sumOfArr = arr[0]
answer = float('inf')

while True:
    if sumOfArr < S:
        front += 1
        if front == N:
            break
        sumOfArr += arr[front]

    else:
        answer = min(answer, front - back+1)
        sumOfArr -= arr[back]
        back += 1


print(answer if answer != float('inf') else 0)
