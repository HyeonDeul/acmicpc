from collections import deque

N = int(input())
arr = list(map(int, input().split()))
mostBigNum = -1
O_arr = deque()
answer = deque()
for i in arr[::-1]:
    if i >= mostBigNum:
        O_arr = deque([i])
        answer.appendleft(-1)
        mostBigNum = i
    else:
        while True:
            now = O_arr[0]
            if i < now:
                answer.appendleft(O_arr[0])
                O_arr.appendleft(i)
                break
            else:
                O_arr.popleft()

print(' '.join(list(map(str, answer))))
