import sys
from collections import deque

row, col = map(int, sys.stdin.readline().split())
graph = []
for _ in range(row):
    graph.append(list(sys.stdin.readline()[:-1]))


drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

q = deque([[0, 0, graph[0][0], 1]])
ans = 0
while q:
    now_row, now_col, visit, cnt = q.popleft()
    for i in range(4):
        next_row = now_row+drow[i]
        next_col = now_col+dcol[i]
        if next_row >= row or next_row < 0 or next_col >= col or next_col < 0:
            continue
        next = graph[next_row][next_col]

        if next not in visit:
            q.appendleft([next_row, next_col, visit+next, cnt+1])
    ans = max(ans, cnt)

print(ans)
