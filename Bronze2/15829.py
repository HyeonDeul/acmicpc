n = int(input())
line = input()
ans = 0
for i in range(n):
    ans += (ord(line[i])-96)*(31**i)
print(ans % 1234567891)
