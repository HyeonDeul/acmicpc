from collections import deque

M, N = map(int, input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int, input())))
temp_graph = [[-1 for _ in range(M)] for _ in range(N)]

temp_graph[0][0] = 0

# 북, 동, 남, 서
drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

queue = deque([[0, 0, 0]])
while queue:
    row, col, brk = queue.popleft()

    for i in range(4):
        next_row = row + drow[i]
        next_col = col + dcol[i]
        temp_brk = brk

        if not 0 <= next_row < N:
            continue
        if not 0 <= next_col < M:
            continue

        if temp_graph[next_row][next_col] == -1:
            if graph[next_row][next_col] == 1:
                temp_brk += 1
            temp_graph[next_row][next_col] = temp_brk
            queue.append([next_row, next_col, temp_brk])

        else:
            if graph[next_row][next_col] == 1:
                temp_brk += 1

            next_brk = temp_graph[next_row][next_col]

            if temp_brk < next_brk:
                temp_graph[next_row][next_col] = temp_brk
                queue.append([next_row, next_col, temp_brk])

print(temp_graph[N-1][M-1])
