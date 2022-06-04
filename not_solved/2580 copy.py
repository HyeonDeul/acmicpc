from collections import deque
import sys
input = sys.stdin.readline


sudoku = []
blank = []
for row in range(9):
    line = list(map(int, input().split()))
    for col in range(9):
        if line[col] == 0:
            blank.append([row, col])
    sudoku.append(line)


def find(row, col, sudoku):
    ver_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    hor_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        ver_now = sudoku[row][i]
        try:
            if 0 < ver_now < 10:
                ver_numbers.remove(ver_now)
        except:
            pass
        hor_now = sudoku[i][col]
        try:
            if 0 < hor_now < 10:
                hor_numbers.remove(hor_now)
        except:
            pass
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(3):
        for j in range(3):
            now = sudoku[3*(row//3)+i][3*(col//3)+j]
            try:
                if 0 < now < 10:
                    numbers.remove(now)
            except:
                pass
    all_num = set(ver_numbers) & set(hor_numbers) & set(numbers)
    return all_num


que = deque([[blank, sudoku]])
answer = []

while que:
    left, graph = que.pop()

    if len(left) == 0:
        answer = graph
        break

    row, col = left.pop()
    can = find(row, col, graph)

    if len(can) == 1:
        graph[row][col] = list(can)[0]
        que.append([left, graph])
    else:
        for c in can:
            temp_left = left[:]
            temp_graph = []
            for g in graph:
                temp_graph.append(g[:])
            temp_graph[row][col] = c
            que.append([temp_left, temp_graph])

for i in answer:
    print(*i)
