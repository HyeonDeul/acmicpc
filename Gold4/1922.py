import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

connections = []
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    connections.append([c, a, b])

connections.sort()
visit = []
cost = 0
for connection in connections:
    c, a, b = connection

    a_idx = -1
    b_idx = -1
    for i in range(len(visit)):
        if a in visit[i]:
            a_idx = i
        if b in visit[i]:
            b_idx = i
    if a_idx == -1 and b_idx == -1:
        visit.append([a, b])
        cost += c
    elif a_idx == -1:
        visit[b_idx].append(a)
        cost += c
    elif b_idx == -1:
        visit[a_idx].append(b)
        cost += c
    elif a_idx == b_idx:
        continue
    else:
        visit[a_idx].extend(visit[b_idx])
        visit.pop(b_idx)
        cost += c
    visit[0].sort()

    if len(set(visit[0])) == N:
        print(cost)
        break
