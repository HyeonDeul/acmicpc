import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())

graph = []
distances1 = []
distances2 = []
distances3 = []
for _ in range(R):
    line = list(map(int, input().rstrip()))
    graph.append(line)
    distances1.append([float('inf') for _ in range(C)])
    distances2.append([float('inf') for _ in range(C)])
    distances3.append([float('inf') for _ in range(C)])
villains = []

for _ in range(3):
    row, col = map(int, input().split())
    villains.append([row-1, col-1])

drow = [-1, 0, 1, 0, 0]
dcol = [0, 1, 0, -1, 0]


def BFS(row, col, distance):
    que = deque([[row, col, 0]])
    distance[row][col] = 0

    while que:
        row, col, dis = que.popleft()
        if distance[row][col] < dis:
            continue
        dis += 1
        for i in range(4):
            nextRow = row+drow[i]
            if not 0 <= nextRow < R:
                continue
            nextCol = col+dcol[i]
            if not 0 <= nextCol < C:
                continue
            if graph[nextRow][nextCol] == 0 and distance[nextRow][nextCol] > dis:
                distance[nextRow][nextCol] = dis
                que.append([nextRow, nextCol, dis])
    return distance


distances1 = BFS(villains[0][0], villains[0][1], distances1)
distances2 = BFS(villains[1][0], villains[1][1], distances2)
distances3 = BFS(villains[2][0], villains[2][1], distances3)

maxDis = 0
for row, col in villains:
    maxDis = max(distances1[row][col], maxDis)
    maxDis = max(distances2[row][col], maxDis)
    maxDis = max(distances3[row][col], maxDis)

if maxDis == float('inf'):
    print(-1)
else:
    ans = (maxDis+1)//2
    print(ans)
    dis1 = []
    dis2 = []
    dis3 = []
    for row in range(R):
        for col in range(C):
            if distances1[row][col] <= ans:
                dis1.append((row, col))
            if distances2[row][col] <= ans:
                dis2.append((row, col))
            if distances3[row][col] <= ans:
                dis3.append((row, col))
    print(len(set(dis1) & set(dis2) & set(dis3)))
