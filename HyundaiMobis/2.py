import sys
import heapq
from tkinter import N

input = sys.stdin.readline

w, h = map(int, input.split())

graph = []
visit = [[0 for _ in range(h)] for _ in range(w)]

sRow, sCol = 0, 0

for i in range(w):
    line = list(map(str, input().rstrip()))
    if 'S' in line:
        sRow = i
        sCol = line.index('S')
    graph.append(line)

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

checkRow = [-1, -1, 1, 1]
checkCol = [-1, 1, -1, 1]

que = [[0, sRow, sCol]]

nextE = False
answer = 0

while que:
    p, row, col = heapq.heappop(que)
    p_cnt = 0

    if visit[row][col] == 1:
        continue
    visit[row][col] = 1

    for i in range(4):
        next_row = row+drow[i]
        if not 0 <= next_row < w:
            continue
        next_col = col+dcol[i]
        if not 0 <= next_col < h:
            continue

        if graph[next_row][next_col] == 'E':
            nextE = True
        elif graph[next_row][next_col] == 'P':
            p_cnt += 1
            heapq.heappush(que, [1, next_row, next_col])
        elif graph[next_row][next_col] == '0':
            heapq.heappush(que, [2, next_row, next_col])

    for i in range(4):
        ch_row = row+checkRow[i]
        if not 0 <= ch_row < w:
            continue
        ch_col = col+checkCol[i]
        if not 0 <= ch_col < h:
            continue
        if graph[ch_row][ch_col] == 'P':
            p_cnt += 1
    if p == 1:
        p_cnt -= 3
    if p == 0:
        p_cnt = 0
    answer += p_cnt

    if nextE:
        break

print(answer)

# ADAS 시스템
# S에서 E로 가는 과정, E가 우선, P도 우선
