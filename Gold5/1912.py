n = int(input())
num = list(map(int, input().split()))
temp = [0 for _ in range(n)]

for i in range(n):
    temp[i] = max(temp[i-1] + num[i], num[i])

print(max(temp))
