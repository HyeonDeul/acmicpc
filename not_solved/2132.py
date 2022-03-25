import sys
from collections import deque


N = int(sys.stdin.readline())
fruits = list(map(int, sys.stdin.readline().split()))
graph = {i: [] for i in range(1, N+1)}
for _ in range(N-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def route(x):
    maxFruit = fruits[x-1]
    queue = deque([[x, fruits[x-1]]])
    visit = []

    while queue:
        now, fruit = queue.pop()
        if maxFruit < fruit:
            maxFruit = fruit

        if now in visit:
            continue

        visit.append(now)
        for next in graph[now]:
            if next not in visit:
                queue.append([next, fruit+fruits[next-1]])
    return maxFruit


maxFruit = 0
maxNode = 1
for i in range(1, N+1):
    nowFruit = route(i)
    if maxFruit < nowFruit:
        maxFruit = nowFruit
        maxNode = i
    # print(i, nowFruit)
print(maxFruit, maxNode)
