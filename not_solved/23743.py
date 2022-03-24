import sys


N, M = map(int, sys.stdin.readline().split())
warps = []

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    warps.append([c, a, b])

escapes = list(map(int, sys.stdin.readline().split()))
for i in range(N):
    warps.append([escapes[i], 0, i+1])
warps.sort()

dis, x, y = warps.pop(0)
totalTime = dis
visit = [[x, y]]

while len(visit[0]) != N+1:
    dis, x, y = warps.pop(0)

    x_idx = -1
    y_idx = -1
    for i in range(len(visit)):
        if x_idx == -1 and x in visit[i]:
            x_idx = i
        if y_idx == -1 and y in visit[i]:
            y_idx = i
        if x_idx != -1 and y_idx != -1:
            break
    if x_idx == y_idx != -1:
        continue
    elif x_idx == y_idx == -1:
        totalTime += dis
        visit.append([x, y])
    elif x_idx == -1:
        totalTime += dis
        visit[y_idx].append(x)
    elif y_idx == -1:
        totalTime += dis
        visit[x_idx].append(y)
    else:
        totalTime += dis
        visit[x_idx].extend(visit[y_idx])
        visit.pop(y_idx)


print(totalTime)