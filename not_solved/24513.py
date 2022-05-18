import sys
input = sys.stdin.readline()

N, M = map(int, input().split())
graph = []
v1 = []
v2 = []
vac = []
for row in range(N):
    line = list(map(int, input().split()))
    for col in range(M):
        if line[i] == 1:
            v1.append([row, col])
        elif line[i] == 2:
            v2.append([row, col])
        elif line[i] == -1:
            vac.append([row, col])
    graph.append(list)
