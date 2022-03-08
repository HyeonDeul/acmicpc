from collections import deque


N, M = map(int, input().split())

graph = []
graph_dis = [[float('inf') for _ in range(M)] for _ in range(N)]

for _ in range(N):
    graph.append(list(map(int, input())))

row, col = 0, 0
graph_dis[0][0] = 1

# 북, 동, 남, 서
drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

# [row, col]
queue = deque([[row, col]])


while queue:
    now_row, now_col = queue.popleft()
    now_dis = graph_dis[now_row][now_col]

    for i in range(4):
        next_row = now_row+drow[i]
        next_col = now_col+dcol[i]

        if not 0 <= next_row < N:
            continue
        if not 0 <= next_col < M:
            continue

        if graph[next_row][next_col] == 1:
            if graph_dis[next_row][next_col] > now_dis+1:
                graph_dis[next_row][next_col] = now_dis+1
                queue.append([next_row, next_col])

print(graph_dis[N-1][M-1])
