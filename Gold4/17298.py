from collections import deque

N = int(input())
arr = list(map(int, input().split()))
O = -1
big = deque()
answer = deque()
for i in arr[::-1]:
    if i >= O:
        big = deque([i])
        answer.appendleft(-1)
        O = i
    else:
        while True:
            now = big[0]
            if i < now:
                answer.appendleft(big[0])
                big.appendleft(i)
                break
            else:
                big.popleft()

print(' '.join(list(map(str, answer))))
