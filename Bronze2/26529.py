dp = [1, 1, 2, 3]
m = int(input())
for _ in range(m):
    n = int(input())
    if len(dp) <= n:
        for i in range(len(dp), n+1):
            dp.append(dp[i-1]+dp[i-2])
    print(dp[n])
