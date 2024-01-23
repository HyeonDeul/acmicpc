N = int(input())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

fish = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            shark = [i, j]
            graph[i][j] = 0
        if graph[i][j] != 0:
            fish += 1

