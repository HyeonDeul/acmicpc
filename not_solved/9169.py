import sys
from collections import deque

while True:
    N, M = map(int, sys.stdin.readline().split())
    if N == 0 and M == 0:
        break

    opinions = [-1]+list(map(int, sys.stdin.readline().rstrip().split()))
    friends = {i: [] for i in range(1, N+1)}

    change = 0
    dif = 0
    for _ in range(M):
        x, y = map(int, sys.stdin.readline().split())
        if opinions[x] != opinions[y]:
            dif += 1
        friends[x].append(y)
        friends[y].append(x)

    queue = deque([])
    for i in range(1, N+1):
        sameValue = 0
        difValue = 0
        now = opinions[i]
        for j in friends[i]:
            if now == opinions[j]:
                sameValue += 1
            else:
                difValue += 1
            if sameValue-difValue+1 < 0:
                queue.append(i)

    while queue:
        sameValue = 0
        difValue = 0
        i = queue.popleft()
        now = opinions[i]
        for j in friends[i]:
            if now == opinions[j]:
                sameValue += 1
            else:
                difValue += 1

        if sameValue-difValue+1 < 0:
            change += 1
            dif += sameValue-difValue
            if now == 1:
                opinions[i] = 0
            else:
                opinions[i] = 1
            queue.extend(friends[i])

    print(dif + change)

# 같 + 1 = 다 : 고민
# 같 + 1 < 다 : 바꾸기
# change+dif > 의견 => 의견 바꾸기
