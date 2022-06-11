import sys

input = sys.stdin.readline

N = int(input())
stars = []
for i in range(N):
    stars.append(list(map(float, input().split())))

dp = [i for i in range(N)]
distances = []
for i in range(N):
    for j in range(N):
        dis = ((stars[i][0]-stars[j][0])**2 +
               (stars[i][1] - stars[j][1])**2)**(1/2)
        distances.append([dis, i, j])
distances.sort()


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
    return find(dp[x])


cnt = 0
all_dis = 0
for dis, x, y in distances:
    fx = find(x)
    fy = find(y)

    if fx == fy:
        continue
    cnt += 1
    all_dis += dis
    union(fx, fy)

    if cnt == N-1:
        break
print(all_dis)
