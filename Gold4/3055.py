import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())
graph = []
disGraph = [[float('inf') for _ in range(C)] for _ in range(R)]

waters = []
for i in range(R):
    temp = list(map(str, sys.stdin.readline().rstrip()))

    for j in range(C):
        if temp[j] == 'S':
            S_row, S_col = i, j
        if temp[j] == 'D':
            D_row, D_col = i, j
        if temp[j] == '*':
            waters.append([i, j])
    graph.append(temp)

disGraph[S_row][S_col] = 0

cnt = 0
drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]
answer = float('inf')

queue = deque([[S_row, S_col, waters, graph]])
while queue:
    nowRow, nowCol, nowWaters, temp = queue.pop()
    nowGraph = [i[:] for i in temp]
    nowCnt = disGraph[nowRow][nowCol]

    new_waters = []
    while nowWaters:
        wr, wc = nowWaters.pop()
        for i in range(4):
            nextWr = wr+drow[i]
            nextWc = wc+dcol[i]
            if not 0 <= nextWr < R:
                continue
            if not 0 <= nextWc < C:
                continue
            if nowGraph[nextWr][nextWc] not in ['D', '*', 'X']:
                nowGraph[nextWr][nextWc] = '*'
                new_waters.append([nextWr, nextWc])
    nowCnt += 1

    for i in range(4):
        nextRow = nowRow+drow[i]
        nextCol = nowCol+dcol[i]
        if not 0 <= nextRow < R:
            continue
        if not 0 <= nextCol < C:
            continue

        next = nowGraph[nextRow][nextCol]
        if next in ['*', 'X']:
            continue
        elif next == 'D':
            if nowCnt < answer:
                answer = nowCnt
        elif nowCnt < disGraph[nextRow][nextCol]:
            disGraph[nextRow][nextCol] = nowCnt
            queue.appendleft([nextRow, nextCol, new_waters[:], nowGraph])

print(answer if answer != float('inf') else 'KAKATUS')
