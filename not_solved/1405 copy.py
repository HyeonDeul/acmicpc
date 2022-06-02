from collections import deque

com, E, W, S, N = map(int, input().split())

direction = [E/100, W/100, S/100, N/100]
drow = [0, 0, 1, -1]
dcol = [1, -1, 0, 0]

row, col = 14, 14
que = deque([[0, row, col, 1, str(row)+','+str(col)]])

answer = 0

while que:
    cnt, row, col, per, visit = que.pop()
    # print(cnt, per)
    if cnt == com:
        answer += per
        continue
    cnt += 1

    for i in range(4):
        if direction[i] != 0:
            next_row = row+drow[i]
            next_col = col+dcol[i]

            temp = str(next_row)+','+str(next_col)
            # if temp in visit:

            if visit.find(temp) == -1:
                print(i)
                que.append([cnt, next_row, next_col, per *
                           direction[i], visit+' '+temp])


print(answer)
