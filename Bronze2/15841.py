dp = [0, 1, 1, 2, 3]
n = int(input())
while (n != -1):
    if len(dp) <= n:
        for i in range(len(dp), n+1):
            dp.append(dp[i-1]+dp[i-2])
    print(f'Hour {n}: {dp[n]} cow(s) affected')
    n = int(input())
