from collections import deque

n, m, k = map(int, input().split())
grid = [[0 for _ in range(m)] for _ in range(n)]
rec = []
rec_size = []

for _ in range(k):
    rec.append(list(map(int, input().split())))

for i in range(k):
    for y in range(n-rec[i][3], n-rec[i][1]):
        for x in range(rec[i][0], rec[i][2]):
            grid[y][x] = 1


drow = [1, 0, -1, 0]  # 남서북동
dcol = [0, -1, 0, 1]

for y in range(n):
    for x in range(m):
        if grid[y][x] == 0:
            queue = deque([[y, x]])
            grid[y][x] = 1
            cnt = 1

            while queue:
                now_row, now_col = queue.popleft()

                for i in range(4):
                    next_row = now_row + drow[i]
                    next_col = now_col + dcol[i]

                    if not 0 <= next_row < n:
                        continue
                    if not 0 <= next_col < m:
                        continue

                    if grid[next_row][next_col] == 0:
                        grid[next_row][next_col] = 1
                        cnt += 1
                        queue.append([next_row, next_col])

            rec_size.append(cnt)

rec_size.sort()
print(*rec_size)
