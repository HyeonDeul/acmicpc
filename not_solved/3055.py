import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
graph = []
route_graph = [[0 for _ in range(N)] for _ in range(M)]
for _ in range(M):
    graph.append(list(map(int, sys.stdin.readline().split())))

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

queue = deque([[0, 0]])
route = 0
while queue:
    row, col = queue.popleft()
    height = graph[row][col]
    now = route_graph[row][col]

    if row == M-1 and col == N-1:
        route += 1
        continue

    for i in range(4):
        nextRow = row+drow[i]
        nextCol = col+dcol[i]

        if not 0 <= nextRow < M:
            continue
        if not 0 <= nextCol < N:
            continue
        if height > graph[nextRow][nextCol]:
            queue.append([nextRow, nextCol])

print(route)
