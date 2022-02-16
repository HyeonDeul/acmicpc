import sys

N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
# 0 북, 1 동, 2 남, 3 서

graph = []

for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

now_row, now_col = r, c
graph[now_row][now_col] = 2
count = 1

leftrow = [0, -1, 0, 1]
leftcol = [-1, 0, 1, 0]

backrow = [1, 0, -1, 0]
backcol = [0, -1, 0, 1]

while True:

    find = False
    for i in range(4):
        if graph[now_row+leftrow[d]][now_col+leftcol[d]] != 0:
            d -= 1
            if d == -1:
                d = 3
        else:
            now_row += leftrow[d]
            now_col += leftcol[d]
            find = True
            d -= 1
            if d == -1:
                d = 3
            break

    if find:
        graph[now_row][now_col] = 2
        count += 1
    # 4방향 다 청소된 경우
    else:
        # 벽인경우
        if d == 4:
            d = 0
        if graph[now_row+backrow[d]][now_col+backcol[d]] == 1:
            break
        # 벽이 아닌 경우
        else:
            now_row += backrow[d]
            now_col += backcol[d]
print(count)
