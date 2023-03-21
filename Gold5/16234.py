import copy


def findUnion(data, N, L, R):
    graph = copy.deepcopy(data)
    drow = [-1, 0, 1, 0]
    dcol = [0, 1, 0, -1]

    unions = []
    for row in range(N):
        for col in range(N):
            for d in range(4):
                nextRow = row + drow[d]
                nextCol = col + dcol[d]

                if nextRow < 0 or nextRow >= N:
                    continue
                if nextCol < 0 or nextCol >= N:
                    continue

                if graph[nextRow][nextCol] == -1:
                    continue

                if L <= abs(graph[row][col]-graph[nextRow][nextCol]) <= R:

                    nowNation = N*row+col
                    nextNation = N*nextRow + nextCol

                    nowIdx = -1
                    nextIdx = -1

                    for i in range(len(unions)):
                        if nowNation in unions[i]:
                            nowIdx = i
                        if nextNation in unions[i]:
                            nextIdx = i

                        if nowIdx != -1 and nextIdx != -1:
                            break

                    if nowIdx == -1 and nextIdx == -1:
                        unions.append([nowNation, nextNation])
                    elif nowIdx == nextIdx:
                        continue
                    elif nowIdx == -1:
                        unions[nextIdx].append(nowNation)
                    elif nextIdx == -1:
                        unions[nowIdx].append(nextNation)
                    else:
                        unions[nowIdx].extend(unions[nextIdx])
                        del unions[nextIdx]
            graph[row][col] = -1
    return unions


N, L, R = map(int, input().split())
populations = []

for i in range(N):
    populations.append(list(map(int, input().split())))

unions = findUnion(populations, N, L, R)
days = 0
while (unions):

    for union in unions:
        sumOfPopulation = 0
        for nation in union:
            row = nation//N
            col = nation % N

            sumOfPopulation += populations[row][col]

        avgOfPopulation = sumOfPopulation//len(union)

        for nation in union:
            row = nation//N
            col = nation % N
            populations[row][col] = avgOfPopulation

    days += 1
    unions = findUnion(populations, N, L, R)

print(days)
