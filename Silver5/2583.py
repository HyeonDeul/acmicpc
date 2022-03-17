from collections import deque
import sys

M, N, K = map(int, sys.stdin.readline().split())
graph = [[0 for _ in range(N)] for _ in range(M)]


for _ in range(K):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

rectangle = []
queue = deque()

for row in range(M):
    for col in range(N):

        if graph[row][col] == 0:
            queue.append([row, col])

            graph[row][col] = 1
            rectangle_size = 1

            while queue:

                nowRow, nowCol = queue.popleft()

                for i in range(4):
                    nextRow = nowRow+drow[i]
                    if not 0 <= nextRow < M:
                        continue
                    nextCol = nowCol+dcol[i]
                    if not 0 <= nextCol < N:
                        continue

                    if graph[nextRow][nextCol] == 0:
                        graph[nextRow][nextCol] = 1
                        rectangle_size += 1
                        queue.append([nextRow, nextCol])
            rectangle.append(rectangle_size)


print(len(rectangle))
rectangle.sort()
for i in rectangle:
    print(i, end=' ')
