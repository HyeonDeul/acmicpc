from collections import deque

N, L, R, X = map(int, input().split())
problems = list(map(int, input().split()))

problems.sort(reverse=True)

answer = 0
queue = deque()
while problems:
    biggest = problems.pop(0)
    if biggest < R:
        # sum, biggest, cnt, arr
        queue.append([biggest, biggest, biggest, 1, problems])

    while queue:
        now, biggest, smallest, cnt, arr = queue.pop()
        if L <= now <= R and cnt > 1:
            if biggest - smallest >= X:
                answer += 1
        l = len(arr)
        for i in range(l):
            num_sum = now+arr[i]
            if num_sum <= R:
                queue.append([num_sum, biggest, arr[i], cnt+1, arr[i+1:]])

print(answer)
