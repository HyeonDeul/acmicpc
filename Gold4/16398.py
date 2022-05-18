import sys
input = sys.stdin.readline

N = int(input())

que = []
for i in range(N):
    temp = list(map(int, input().split()))

    for j in range(i+1, N):
        que.append([temp[j], i, j])

que.sort()
total_cost, x, y = que[0]
visit = [[x, y]]

for idx in range(1, len(que)):
    cost, x, y = que[idx]
    idx_x = -1
    idx_y = -1
    for i in range(len(visit)):
        if x in visit[i]:
            idx_x = i
        if y in visit[i]:
            idx_y = i
        if idx_x != -1 and idx_y != -1:
            break

    if idx_x == -1 and idx_y == -1:
        visit.append([x, y])
    elif idx_x == -1:
        visit[idx_y].append(x)
    elif idx_y == -1:
        visit[idx_x].append(y)
    elif idx_x == idx_y:
        continue
    else:
        visit[idx_x].extend(visit[idx_y])
        visit.pop(idx_y)
    total_cost += cost

    if len(visit[0]) == N:
        break

print(total_cost)
