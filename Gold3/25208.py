import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = []


for row in range(N):
    line = list(map(str, input().rstrip()))
    for col in range(M):
        if line[col] == 'D':
            D_row = row
            D_col = col
        elif line[col] == 'R':
            R_row = row
            R_col = col
    graph.append(line)


def calSide(side, row, col):
    # 상, 우, 하, 좌
    mov = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    # 0 바닥, 1 위, 2 북, 3 동, 4 남, 5 서

    if side == 0:
        if mov.index([row, col]) == 0:
            return 4
        elif mov.index([row, col]) == 1:
            return 5
        elif mov.index([row, col]) == 2:
            return 2
        elif mov.index([row, col]) == 3:
            return 3
    elif side == 1:
        if mov.index([row, col]) == 0:
            return 2
        elif mov.index([row, col]) == 1:
            return 3
        elif mov.index([row, col]) == 2:
            return 4
        elif mov.index([row, col]) == 3:
            return 5
    elif side == 2:
        if mov.index([row, col]) == 0:
            return 0
        elif mov.index([row, col]) == 1:
            return 2
        elif mov.index([row, col]) == 2:
            return 1
        elif mov.index([row, col]) == 3:
            return 2
    elif side == 3:
        if mov.index([row, col]) == 0:
            return 3
        elif mov.index([row, col]) == 1:
            return 0
        elif mov.index([row, col]) == 2:
            return 3
        elif mov.index([row, col]) == 3:
            return 1
    elif side == 4:
        if mov.index([row, col]) == 0:
            return 1
        elif mov.index([row, col]) == 1:
            return 4
        elif mov.index([row, col]) == 2:
            return 0
        elif mov.index([row, col]) == 3:
            return 4
    else:
        if mov.index([row, col]) == 0:
            return 5
        elif mov.index([row, col]) == 1:
            return 1
        elif mov.index([row, col]) == 2:
            return 5
        elif mov.index([row, col]) == 3:
            return 0


drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

distances = [[[float('inf') for _ in range(6)]
              for _ in range(M)] for _ in range(N)]

distances[D_row][D_col][0] = 0
que = deque([[D_row, D_col, 0, 0]])

# 0 바닥, 1 위, 2 북, 3 동, 4 남, 5 서
while que:
    row, col, side, dis = que.popleft()

    if distances[row][col][side] < dis:
        continue
    elif side == 0 and row == R_row and col == R_col:
        continue

    dis += 1

    for i in range(4):
        next_row, next_col = row+drow[i], col+dcol[i]

        new_side = calSide(side, drow[i], dcol[i])
        if new_side != 0 and next_row == R_row and next_col == R_col:
            continue
        elif graph[next_row][next_col] == '#':
            continue
        elif distances[next_row][next_col][new_side] > dis:
            distances[next_row][next_col][new_side] = dis
            que.append([next_row, next_col, new_side, dis])

answer = distances[R_row][R_col][0]

print(answer if answer != float('inf') else -1)
