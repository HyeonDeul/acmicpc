V, E = map(int, input().split())

route = []
for _ in range(E):
    a, b, c = map(int, input().split())

    route.append([c, a, b])

route.sort()

visit = []
ans = 0

for dis, no1, no2 in route:

    idx1 = -1
    idx2 = -1

    for i in range(len(visit)):
        if no1 in visit[i]:
            idx1 = i
        if no2 in visit[i]:
            idx2 = i

    if idx1 == -1 and idx2 == -1:
        visit.append([no1, no2])
        ans += dis
    elif idx1 == idx2:
        continue
    elif idx1 == -1:
        visit[idx2].append(no1)
        ans += dis
    elif idx2 == -1:
        visit[idx1].append(no2)
        ans += dis
    else:
        visit[idx1].extend(visit[idx2])
        visit.pop(idx2)
        ans += dis

    if len(visit[0]) == V:
        break

print(ans)
