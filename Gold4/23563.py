from operator import ne
import sys
from collections import deque
input = sys.stdin.readline

H, W = map(int, input().split())

graph = []
for i in range(H):
    line = list(map(str, input().rstrip()))
    for j in range(W):
        if 'S' == line[j]:
            row, col = i, j
        if 'E' == line[j]:
            end_row, end_col = i, j
    graph.append(line)

graph[row][col] = 0
graph[end_row][end_col] = '.'
drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

isWall = False
for i in range(4):
    next_row = row+drow[i]
    if not 0 <= next_row < H:
        continue
    next_col = col+dcol[i]
    if not 0 <= next_col < W:
        continue
    if graph[next_row][next_col] == '#':
        isWall = True
        break

que = deque([[row, col, 0, isWall]])

while que:
    row, col, dis, isWall = que.pop()
    if graph[row][col] != '.' and graph[row][col] < dis:
        continue

    for i in range(4):
        next_row = row+drow[i]
        if not 0 <= next_row < H:
            continue
        next_col = col+dcol[i]
        if not 0 <= next_col < W:
            continue

        if graph[next_row][next_col] == '#':
            continue
        else:
            isWallToo = False
            for j in range(4):
                new_row = next_row+drow[j]
                if not 0 <= new_row < H:
                    continue
                new_col = next_col + dcol[j]
                if not 0 <= new_col < W:
                    continue
                if graph[new_row][new_col] == '#':
                    isWallToo = True
                    break

            if isWall and isWallToo:
                if graph[next_row][next_col] == '.':
                    graph[next_row][next_col] = dis
                    que.append([next_row, next_col, dis, isWallToo])
                elif graph[next_row][next_col] > dis:
                    graph[next_row][next_col] = dis
                    que.append([next_row, next_col, dis, isWallToo])
            else:
                if graph[next_row][next_col] == '.':
                    graph[next_row][next_col] = dis+1
                    que.append([next_row, next_col, dis+1, isWallToo])
                elif graph[next_row][next_col] > dis+1:
                    graph[next_row][next_col] = dis+1
                    que.append([next_row, next_col, dis+1, isWallToo])


for i in graph:
    print(i)
print(graph[end_row][end_col])
