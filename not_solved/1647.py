import sys
input = sys.stdin.readline

N, M = map(int, input().split())
roads = []

for _ in range(M):
    a, b, c = map(int, input().split())
    roads.append([c, a, b])

roads.sort()
totalCost = 0
cities = []

for cost, x, y in roads:

    xIdx, yIdx = -1, -1

    for i in range(len(cities)):
        if xIdx == -1 and x in cities[i]:
            xIdx = i
        if yIdx == -1 and y in cities[i]:
            yIdx = i
        if xIdx != -1 and yIdx != -1:
            break

    if xIdx == -1 and yIdx == -1:
        cities.append([x, y])
    elif xIdx == yIdx:
        continue
    elif xIdx == -1 and yIdx != -1:
        cities[yIdx].append(x)
    elif xIdx != -1 and yIdx == -1:
        cities[xIdx].append(y)
    else:
        cities[xIdx].extend(cities[yIdx])
        cities.pop(yIdx)

    totalCost += cost
    if len(cities[0]) == N:
        totalCost -= cost
        break

print(totalCost)
