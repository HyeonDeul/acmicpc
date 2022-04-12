import sys
n = int(sys.stdin.readline())

arr = []
for _ in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    arr.append(line)
arr.sort(key=lambda x: x[0])
arr.sort(key=lambda x: x[1])

last = -1
cnt = 0

for i, j in arr:
    if i >= last:
        last = j
        cnt += 1

print(cnt)
