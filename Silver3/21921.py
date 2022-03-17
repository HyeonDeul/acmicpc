N, X = map(int, input().split())
visit = list(map(int, input().split()))

maxVisit = sum(visit[:X])
maxDay = 1
now = maxVisit
for i in range(N-X):
    now += visit[i+X]-visit[i]
    if maxVisit < now:
        maxVisit = now
        maxDay = 1
    elif maxVisit == now:
        maxDay += 1

if maxVisit == 0:
    print("SAD")
else:
    print(maxVisit)
    print(maxDay)
