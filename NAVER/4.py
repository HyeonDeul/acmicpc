from collections import deque


def solution(B):
    ans = [0, 0, 0]

    maxRow = len(B)
    maxCol = len(B[0])

    graph = []
    for i in B:
        graph.append(list(map(str, i)))

    drow = [-1, 0, 1, 0]
    dcol = [0, 1, 0, -1]

    for row in range(maxRow):
        for col in range(maxCol):
            if graph[row][col] == '#':
                ship = 1
                shipque = deque([[row, col]])
                while shipque:
                    trow, tcol = shipque.pop()

                    for i in range(4):
                        next_row = trow+drow[i]
                        graph[trow][tcol] = 'X'
                        if not 0 <= next_row < maxRow:
                            continue
                        next_col = tcol+dcol[i]
                        if not 0 <= next_col < maxCol:
                            continue
                        if graph[next_row][next_col] == '#':
                            ship += 1
                            shipque.append([next_row, next_col])
                ans[ship-1] += 1
    return ans


print(solution(['.##.#', '#.#..', '#...#', '#.##.']))
