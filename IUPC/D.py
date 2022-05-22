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

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

que = deque([[D_row, D_col, 0, 0, 0]])
dis = [[float('inf') for _ in range(M)] for _ in range(N)]

# while que:
#     row, col, cnt, dice, up, side = que.pop()

#     for i in range(4):
#         next_row = row+drow[i]
#         if not 0 <= next_row < N:
#             continue
#         next_col = col+dcol[i]
#         if not 0 <= next_col < M:
#             continue
#         if graph[next_row][next_col] == '.':
#             que.append([next_row, next_col, cnt+1])
#         elif graph[next_row][next_col] == 'R':
#             print()

print(1)
