from collections import deque
import sys
input = sys.stdin.readline

sudoku = []
blank = deque()
l_blank = 0
for row in range(9):
    line = list(map(int, input().split()))
    for col in range(9):
        if line[col] == 0:
            blank.append([row, col])
            l_blank += 1
    sudoku.append(line)


def find(row, col, sudoku):
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        ver_now = sudoku[row][i]
        if ver_now in nums:
            nums.remove(ver_now)
        hor_now = sudoku[i][col]
        if hor_now in nums:
            nums.remove(hor_now)
    for i in range(3):
        for j in range(3):
            now = sudoku[3*(row//3)+i][3*(col//3)+j]
            if now in nums:
                nums.remove(now)
    return nums


que = deque([[0, sudoku]])

isSolved = False
while que:
    if isSolved:
        break
    idx, graph = que.pop()
    row, col = blank[idx]
    idx += 1
    nums = find(row, col, graph)

    for v in nums:
        if isSolved:
            break
        graph[row][col] = v
        if idx == l_blank:
            for i in graph:
                print(*i)
            isSolved = True
            break
        else:
            temp_graph = [g[:] for g in graph]
            que.append([idx, temp_graph])
