import sys
n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

x, y = arr[0]
rank = [[x, y, x, y, 1]]

for a in arr[1:]:
    x1, y1 = a
    inserted = False
    for i in range(len(rank)):
        x2, y2, x3, y3, cnt = rank[i]

        if x1 > x2 and y1 > y2:
            rank.insert(i, [x1, y1, x1, y1, 1])
            inserted = True
            break
        elif x1 < x3 and y1 < y3:
            continue
        else:
            inserted = True
            rank[i] = [max(x1, x2), max(y1, y2), min(
                x1, x3), min(y1, y3), cnt+1]
    if not inserted:
        rank.append([x1, y1, x1, y1, 1])
prev = 1
for i in range(n):
    x1, y1 = arr[i]
    idx = -1
    for j in range(len(rank)):
        x2, y2, x3, y3, cnt = rank[j]
        if x3 <= x1 <= x2 and y3 <= y1 <= y2:
            idx = j+prev
        prev = cnt

    arr[i] = idx
print(*arr)
