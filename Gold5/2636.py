import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

graph = []
cheeses = deque([])
temp_holes = deque([])

for row in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    if 1 in line:
        openning = False
        notclose = 0
        for col in range(M):
            if line[col] == 1:
                cheeses.append([row, col])
                openning = True
                notclose = 0
            else:
                if openning:
                    temp_holes.append([row, col])
                    notclose += 1
        for _ in range(notclose):
            temp_holes.pop()

    graph.append(line)

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

inner_holes = []
while temp_holes:
    isIn = True
    row, col = temp_holes.popleft()
    hole = [[row, col]]
    queue = deque([[row, col]])

    while queue:
        now_row, now_col = queue.popleft()
        for i in range(4):
            next_row = now_row+drow[i]
            if not 0 <= next_row < N:
                continue
            next_col = now_col+dcol[i]
            if not 0 <= next_col < M:
                continue
            if graph[next_row][next_col] == 0:
                if [next_row, next_col] in temp_holes:
                    temp_holes.remove([next_row, next_col])
                    hole.append([next_row, next_col])
                    queue.append([next_row, next_col])
                elif [next_row, next_col] not in hole:
                    isIn = False
    if isIn:
        inner_holes.append(hole)

print(inner_holes)


# hour = 0
# size = len(cheeses)


# while cheeses:
#     while cheeses:
#         row, col = cheeses.popleft()
#         for i in range(4):
#             next_row = row+drow[i]
#             if not 0 <= next_row < N:
#                 continue
#             next_col = col+dcol[i]
#             if not 0 <= next_col < M:
#                 continue
#             if graph[]
