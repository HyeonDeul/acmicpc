from collections import deque
import copy

sudoku = []

blank = []
for row in range(9):
    line = list(map(int, input().split()))
    for col in range(9):
        if line[col] == 0:
            blank.append([row, col])
    sudoku.append(line)


def find(row, col, sudoku):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        now = sudoku[row][i]
        try:
            if 0 < now < 10:
                numbers.remove(now)
        except:
            pass
    all_num = set(numbers)

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        now = sudoku[i][col]
        try:
            if 0 < now < 10:
                numbers.remove(now)
        except:
            pass
    all_num = all_num & set(numbers)

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(3):
        for j in range(3):
            now = sudoku[3*(row//3)+i][3*(col//3)+j]
            try:
                if 0 < now < 10:
                    numbers.remove(now)
            except:
                pass
    all_num = all_num & set(numbers)

    return all_num


temp = deque()
for row, col in blank:
    num = list(find(row, col, sudoku))
    if len(num) == 1:
        sudoku[row][col] = num[0]
    else:
        sudoku[row][col] = num
        temp.append([row, col])

if len(temp) == 0:
    answer = copy.deepcopy(sudoku)
else:
    answer = []
que = deque([[temp, sudoku]])


while que:
    left, graph = que.pop()

    if len(left) == 0:
        answer = copy.deepcopy(graph)
        break

    row, col = left.popleft()

    can = list(find(row, col, graph))
    for c in can:
        temp_graph = copy.deepcopy(graph)
        temp_graph[row][col] = c
        temp_left = copy.deepcopy(left)
        que.append([temp_left, temp_graph])

for i in answer:
    print(*i)
