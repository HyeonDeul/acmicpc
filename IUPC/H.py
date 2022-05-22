# 배열 길이 보다 작은 정수 중
# i번째로 추가한 정수와 그 다음에 추가한 정 수 중
# 다음 빼기 이번 정수의 최대 값을 구한다.

N = int(input())
dp = [-1 for _ in range(N)]

arr = list(map(int, input().split()))
minValue = arr[0]
dp[0] = 0
for i in range(1, N):
    maxgap = arr[i]-minValue

    if dp[i-1] > maxgap:
        dp[i] = dp[i-1]
    else:
        dp[i] = maxgap
    minValue = min(minValue, arr[i])
print(*dp)
