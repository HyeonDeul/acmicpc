import sys
from collections import deque
import copy
input = sys.stdin.readline

R, C, K = map(int, input().split())
graph = []
temp = []
for _ in range(R):
    graph.append(list(map(str, input())))
    temp.append([0 for _ in range(C)])


row, col = R-1, 0
que = deque([[row, col, 1, temp]])
temp[row][col] = -1

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]
cnt = 0
while que:
    row, col, dis, now_graph = que.pop()
    if dis == K:
        if row == 0 and col == C-1:
            cnt += 1
        else:
            continue
    dis += 1

    for i in range(4):
        next_row = row+drow[i]
        if not 0 <= next_row < R:
            continue
        next_col = col+dcol[i]
        if not 0 <= next_col < C:
            continue

        if graph[next_row][next_col] != 'T' and now_graph[next_row][next_col] != -1:
            next_graph = copy.deepcopy(now_graph)
            next_graph[next_row][next_col] = -1
            que.append([next_row, next_col, dis, next_graph])

print(cnt)
