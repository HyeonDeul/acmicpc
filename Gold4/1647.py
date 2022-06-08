import sys
input = sys.stdin.readline

N, M = map(int, input().split())
roads = []

for _ in range(M):
    a, b, c = map(int, input().split())
    roads.append([c, a, b])

roads.sort()
totalCost = 0
cities = []

dp = [i for i in range(N+1)]


def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        dp[y] = x
    else:
        dp[x] = y


def find(x):
    if dp[x] == x:
        return x
    else:
        return find(dp[x])


cnt = 1

for cost, x, y in roads:
    if find(x) == find(y):
        continue
    # print(dp, x, y, cost)
    totalCost += cost
    cnt += 1
    union(x, y)
    if cnt == N:
        totalCost -= cost
        print(totalCost)
        break
