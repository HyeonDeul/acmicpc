import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().split())

box = [[] for _ in range(H)]
tomatos = deque([])
not_tomatos = 0

for i in range(N*H):
    line = list(map(int, sys.stdin.readline().split()))
    line_len = len(line)
    for j in range(line_len):
        if line[j] == 1:
            tomatos.append([i//N, i % N, j])
        elif line[j] == 0:
            not_tomatos += 1
    box[i//N].append(line)
# floor, row, col

d_height = [1, -1, 0, 0, 0, 0]
d_row = [0, 0, -1, 0, 1, 0]
d_col = [0, 0, 0, 1, 0, -1]
day = 0
while tomatos and not_tomatos != 0:
    day += 1
    len_tomatos = len(tomatos)
    for _ in range(len_tomatos):
        height, row, col = tomatos.popleft()

        for i in range(6):
            next_height = height+d_height[i]
            if not 0 <= next_height < H:
                continue
            next_row = row+d_row[i]
            if not 0 <= next_row < N:
                continue
            next_col = col+d_col[i]
            if not 0 <= next_col < M:
                continue

            if box[next_height][next_row][next_col] == 0:
                box[next_height][next_row][next_col] = 1
                not_tomatos -= 1
                tomatos.append([next_height, next_row, next_col])

print(-1 if not_tomatos != 0 else day)
