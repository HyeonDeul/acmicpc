
from collections import deque


def solution(place):
    answer = []
    drow = [-1, 0, 1, 0]
    dcol = [0, 1, 0, -1]

    for graph in place:
        distance = True
        people = []
        for i in range(5):
            for j in range(5):
                if graph[i][j] == 'P':
                    people.append([i, j])

        for per in people:
            if not distance:
                break

            r, c = per
            que = deque([[r, c, 0]])
            temp = list(graph[r])
            temp[c] = 'X'
            graph[r] = ''.join(temp)

            while que:
                row, col, dis = que.pop()
                if dis > 2:
                    continue

                for t in range(4):
                    next_row = row+drow[t]
                    next_col = col+dcol[t]
                    if not 0 <= next_row <= 4:
                        continue
                    if not 0 <= next_col <= 4:
                        continue
                    if graph[next_row][next_col] == 'P':
                        if dis+1 <= 2:
                            que = deque([])
                            distance = False
                            break
                    elif graph[next_row][next_col] == 'O':
                        if dis+1 < 2:
                            que.append([next_row, next_col, dis+1])
            temp = list(graph[r])
            temp[c] = 'P'
            graph[r] = ''.join(temp)

        if distance:
            answer.append(1)
        else:
            answer.append(0)
    return answer


s = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP",
                                                                                                    "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(s))
