import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

# graph = []
# ices = []
graph = deque()
ices = deque()

for i in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    for j in range(len(line)):
        if line[j] != 0:
            ices.append([i, j])
    graph.append(line)

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]
splitIce = False
answer = 0
while not splitIce:
    minIce = float('inf')
    # 최소 값 찾기
    for i in ices:
        row, col = i
        now = graph[row][col]

        waters = 0
        for j in range(4):
            next_row = row+drow[j]
            next_col = col+dcol[j]

            if not 0 <= next_row < N:
                continue
            if not 0 <= next_col < M:
                continue

            if graph[next_row][next_col] == 0:
                waters += 1

        if waters != 0:
            melting = now//waters
            if now % waters != 0:
                melting += 1

            if melting < minIce:
                minIce = melting
        graph[row][col] = [graph[row][col], waters]

    # 값 빼기
    l = len(ices)
    idx = 0
    while idx < l:
        row, col = ices[idx]
        now, waters = graph[row][col]
        graph[row][col] = now-(minIce*waters)

        if graph[row][col] <= 0:
            graph[row][col] = 0
            # print(ices.pop(idx))
            ices.remove([row, col])
            l -= 1
        else:
            idx += 1
    answer += minIce
    if len(ices) <= 1:
        splitIce = True
    else:
        visit = deque([ices[0]])
        queue = deque([ices[0]])
        while queue:
            row, col = queue.popleft()
            for i in range(4):
                next_row = row+drow[i]
                next_col = col+dcol[i]

                if not 0 <= next_row < N:
                    continue
                if not 0 <= next_col < M:
                    continue
                if graph[next_row][next_col] != 0:
                    if [next_row, next_col] not in visit:
                        visix`t.appendleft([next_row, next_col])
                        queue.appendleft([next_row, next_col])
        if len(visit) != len(ices):
            splitIce = True

print(answer)
