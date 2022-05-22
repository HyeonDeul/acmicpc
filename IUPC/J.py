import sys
from collections import deque

input = sys.stdin.readline

N, M, T = map(int, input().split())
room = deque([0])
for _ in range(N):
    room.append(list(map(int, input().split())))

graph = [deque() for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)

que = deque([[1, 0, 0, 0]])

maxMoney = 0
needDeff = 0

timegraph = [[-1 for _ in range(N)] for _ in range(T)]
visitgraph = [[float('inf') for _ in range(N)] for _ in range(T)]

while que:
    now, time, money, deff = que.popleft()
    if timegraph[time][now-1] > money:
        continue
    elif timegraph[time][now-1] == money:
        if visitgraph[time][now-1] < deff:
            continue
    visitgraph[time][now-1] = deff
    a, x, y, c = room[now]
    need = (a+x*time)//y if (a+x*time) % y == 0 else (a+x*time) // y+1

    deff = deff if deff > need else need
    time += 1
    money += c

    if time == T or len(graph[now]) == 0:
        if maxMoney < money:
            maxMoney = money
            needDeff = deff
        elif maxMoney == money:
            needDeff = needDeff if needDeff < deff else deff
        continue

    for i in graph[now]:
        if timegraph[time][i-1] < money:
            timegraph[time][i-1] = money
            visitgraph[time][i-1] = float('inf')
            que.append([i, time, money, deff])
        elif timegraph[time][i-1] == money:
            if visitgraph[time][i-1] > deff:
                visitgraph[time][i-1] = float('inf')
                que.append([i, time, money, deff])

print(needDeff)
