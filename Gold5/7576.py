import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
graph = []
tomatos = deque()
left_tomatos = 0
for row in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    for col in range(M):
        if line[col] == 1:
            tomatos.append([row, col])
        elif line[col] == 0:
            left_tomatos += 1
    graph.append(line)

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]
day = -1
while tomatos:
    next_tomatos = deque()
    while tomatos:
        row, col = tomatos.pop()
        for i in range(4):
            next_row = row+drow[i]
            if not 0 <= next_row < N:
                continue
            next_col = col+dcol[i]
            if not 0 <= next_col < M:
                continue

            if graph[next_row][next_col] == 0:
                graph[next_row][next_col] = 1
                left_tomatos -= 1
                next_tomatos.append([next_row, next_col])

    day += 1
    tomatos = next_tomatos

print(-1 if left_tomatos else day)
