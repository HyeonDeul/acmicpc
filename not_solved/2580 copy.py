from collections import deque
import copy

sudoku = []

blank = 0
blankList = []
for row in range(9):
    line = list(map(int, input().split()))
    for col in range(9):
        if line[col] == 0:
            blank += 1
            blankList.append([row, col])
    sudoku.append(line)


def hori(row, sudoku, blank):
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    changeList = []
    for i in range(9):
        try:
            if 0 < sudoku[row][i] < 10:
                nums.remove(sudoku[row][i])
            else:
                changeList.append(i)
        except:
            changeList.append(i)
    for i in changeList:
        if sudoku[row][i] == 0:
            sudoku[row][i] = nums
        else:
            sudoku[row][i] = list(set(nums) & set(sudoku[row][i]))
        if len(sudoku[row][i]) == 1:
            sudoku[row][i] = sudoku[row][i][0]
            blank -= 1
            blankList.remove([row, i])
    return sudoku, blank


def verti(col, sudoku, blank):
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    changeList = []
    for i in range(9):
        try:
            if 0 < sudoku[i][col] < 10:
                nums.remove(sudoku[i][col])
            else:
                changeList.append(i)
        except:
            changeList.append(i)
    for i in changeList:
        if sudoku[i][col] == 0:
            sudoku[i][col] = nums
        else:
            sudoku[i][col] = list(set(nums) & set(sudoku[i][col]))
        if len(sudoku[i][col]) == 1:
            sudoku[i][col] = sudoku[i][col][0]
            blank -= 1
            blankList.remove([i, col])
    return sudoku, blank


def square(row, col, sudoku, blank):
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    changeList = []
    for i in range(3):
        for j in range(3):
            now = sudoku[3*row+i][3*col+j]
            try:
                if 0 < now < 10:
                    nums.remove(now)
                else:
                    changeList.append([3*row+i, 3*col+j])
            except:
                changeList.append([3*row+i, 3*col+j])
    for r, c in changeList:
        if sudoku[r][c] == 0:
            sudoku[r][c] = nums
        else:
            sudoku[r][c] = list(set(nums) & set(sudoku[r][c]))
        if len(sudoku[r][c]) == 1:
            sudoku[r][c] = sudoku[r][c][0]
            blank -= 1
            blankList.remove([r, c])
    return sudoku, blank


origin = copy.deepcopy(sudoku)
for i in range(9):
    sudoku, blank = hori(i, sudoku, blank)
for i in range(9):
    sudoku, blank = verti(i, sudoku, blank)
for i in range(3):
    for j in range(3):
        sudoku, blank = square(i, j, sudoku, blank)

while origin != sudoku:
    origin = copy.copy(sudoku)
    for i in range(9):
        sudoku, blank = hori(i, sudoku, blank)
    if blank == 0:
        break
    for i in range(9):
        sudoku, blank = verti(i, sudoku, blank)
    if blank == 0:
        break
    for i in range(3):
        for j in range(3):
            sudoku, blank = square(i, j, sudoku, blank)


for i in sudoku:
    print(*i)
