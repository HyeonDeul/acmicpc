from itertools import combinations

n = int(input())
arr = list(map(int, input().split()))
for i in range(n):
    arr[i] = 1/arr[i]

cnt = 0

for i in range(2, n+1):
    for com in combinations(arr, i):
        if 99/100 <= sum(com) <= 101/100:
            cnt += 1

print(cnt)