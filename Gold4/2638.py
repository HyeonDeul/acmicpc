import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
cheeses = []

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

for _ in range(N):
    line = list(map(int, input().split()))
    graph.append(line)

que = deque([[0, 0]])


def change(row, col, x, y):
    que = deque([[row, col]])

    while que:
        row, col = que.pop()
        if graph[row][col] == y:
            continue
        graph[row][col] = y

        for i in range(4):
            nextRow = row+drow[i]
            if not 0 <= nextRow < N:
                continue
            nextCol = col+dcol[i]
            if not 0 <= nextCol < M:
                continue

            if graph[nextRow][nextCol] == x:
                que.append([nextRow, nextCol])


def melting(cheeses):
    meltingList = []
    for row, col in cheeses:
        side = 0
        for i in range(4):
            if graph[row+drow[i]][col+dcol[i]] == -1:
                side += 1
        if side >= 2:
            meltingList.append([row, col])
    return meltingList


change(0, 0, 0, -1)

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            cheeses.append([i, j])

cnt = 0
melting_list = melting(cheeses)
while melting_list:
    cnt += 1
    for row, col in melting_list:
        cheeses.remove([row, col])
        graph[row][col] = -1
        for i in range(4):
            nextRow = row+drow[i]
            nextCol = col+dcol[i]
            if graph[nextRow][nextCol] == 0:
                change(nextRow, nextCol, 0, -1)
        melting_list = melting(cheeses)


print(cnt)
