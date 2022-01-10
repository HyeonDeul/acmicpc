def combi(N, start, end, prev=[]):
    all_set = []

    numList = [i for i in range(start, end)]
    for i in numList:
        temp = prev[:]
        temp.append(i)
        if N == 1:
            all_set.append(temp)
        else:
            all_set.extend(combi(N-1, i+1, end, temp))

    return all_set


N, M = map(int, input().split())


graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

house = []
chicken = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            house.append([i, j])
        elif graph[i][j] == 2:
            chicken.append([i, j])

distance_chicken = {}
for i in range(len(chicken)):
    distance_chicken[i] = []
    for j in range(len(house)):
        distance_chicken[i].append(abs(chicken[i][0]-house[j][0]) +
                                   abs(chicken[i][1]-house[j][1]))

for_list = combi(M, 0, len(distance_chicken))

map_dis = float('inf')
for i in for_list:
    temp = 0

    for j in range(len(house)):  # 집 개수만큼
        mindis = float('inf')
        for k in i:  # 치킨집 개수
            if mindis > distance_chicken[k][j]:
                mindis = distance_chicken[k][j]
        temp += mindis
    if temp < map_dis:
        map_dis = temp

print(map_dis)
