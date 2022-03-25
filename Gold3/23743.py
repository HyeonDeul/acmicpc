import sys


N, M = map(int, sys.stdin.readline().split())
warps = []
parants = [i for i in range(N+1)]


def find(x):
    if x != parants[x]:
        parants[x] = find(parants[x])
    return parants[x]


def union(x, y):
    root1 = find(x)
    root2 = find(y)
    parants[root2] = root1


for _ in range(M):
    warps.append(list(map(int, sys.stdin.readline().split())))

escapes = list(map(int, sys.stdin.readline().split()))
for i in range(N):
    warps.append([0, i+1, escapes[i]])

warps.sort(key=lambda x: x[2])

edges = 0
totalTime = 0

while edges != N:
    x, y, dis = warps.pop(0)
    if find(x) != find(y):
        union(x, y)
        totalTime += dis
        edges += 1

print(totalTime)
