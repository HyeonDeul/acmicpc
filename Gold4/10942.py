import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)

dp = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(N+1):
    dp[0][i] = 1

que = deque()
for i in range(1, N+1):
    dp[i][i] = 1
    que.append([i, i])
for i in range(N):
    if arr[i] == arr[i+1]:
        dp[i][i+1] = 1
        que.append([i, i+1])

while que:
    S, E = que.pop()
    S, E = S-1, E+1
    if S < 1 or E > N:
        continue

    if arr[S] == arr[E]:
        dp[S][E] = 1
        que.append([S, E])

M = int(input())
for _ in range(M):
    S, E = map(int, input().split())
    print(dp[S][E])
