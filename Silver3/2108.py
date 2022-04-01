import sys
N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]
arr.sort()
print(round(sum(arr)/N))
print(arr[N//2])
answer = []
acnt = 0
t = arr[0]
tcnt = 0

for i in arr:
    if i == t:
        tcnt += 1
    else:
        if tcnt == acnt:
            answer.append(t)
        elif acnt < tcnt:
            answer = [t]
            acnt = tcnt
        t = i
        tcnt = 1
if tcnt == acnt:
    answer.append(t)
elif acnt < tcnt:
    answer = [t]
    acnt = tcnt

print(answer[0] if len(answer) == 1 else answer[1])

print(arr[N-1]-arr[0])
