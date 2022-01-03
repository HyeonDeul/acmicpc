from collections import deque

v, e = map(int, input().split())
tree = {i: [] for i in range(1, v+1)}

for _ in range(e):
    a, b, c = map(int, input().split())

    tree[a].append([b, c])
    tree[b].append([a, c])


q = deque([[1, [], 0]])

min_spanning = float('inf')
full = [i for i in range(1, v+1)]
while q:
    now, visit, dis = q.pop()
    visit.append(now)
    print(now, visit, dis)

    if visit == full:
        if min_spanning > dis:
            min_spanning = dis
    else:
        for next, nextdis in tree[now]:
            if next in visit:
                continue

            q.append([next, visit[:], dis+nextdis])

print(min_spanning)
