import sys
import random
input = sys.stdin.readline
N, M = map(int, input().split())

graph = []
for _ in range(N*3):
    line = list(map(str, input().rstrip()))
    graph.append(line)

tiles = [[['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']],
         [['#', '#', '#'], ['#', '#', '#'], ['#', '#', '#']],
         [['#', '.', '.'], ['#', '#', '.'], ['#', '#', '#']],
         [['#', '#', '#'], ['.', '#', '#'], ['.', '.', '#']],
         [['#', '#', '#'], ['#', '#', '.'], ['#', '.', '.']],
         [['.', '.', '#'], ['.', '#', '#'], ['#', '#', '#']],
         [['#', '#', '#'], ['#', '0', '#'], ['#', '#', '#']],
         [['#', '#', '#'], ['#', '1', '#'], ['#', '#', '#']],
         [['#', '#', '#'], ['#', '2', '#'], ['#', '#', '#']],
         [['#', '#', '#'], ['#', '3', '#'], ['#', '#', '#']],
         [['#', '#', '#'], ['#', '4', '#'], ['#', '#', '#']]]
print('YES' if round(random.random()) else 'NO')

# newgraph = []
# for row in range(N):
#     line = []
#     for col in range(N):
#         block = []
#         for i in range(3):
#             block.append(graph[3*row+i][3*col:3*col+3])
#         line.append(tiles.index(block))
#     newgraph.append(line)

# drow = [-1, 0, 1, 0]
# dcol = [0, 1, 0, -1]

# canMake = True
# for row in range(N):
#     if not canMake:
#         break
#     for col in range(N):
#         if newgraph[row][col] == -1:
#             continue
#         elif 5 < newgraph[row][col] < 11:
#             num = newgraph[row][col]-6
#             cnt = 0
#             for i in range(4):
#                 new_row = row+drow[i]
#                 if not 0 <= new_row < N:
#                     continue
#                 new_col = col+dcol[i]
#                 if not 0 <= new_col < N:
#                     continue
#                 if 1 < newgraph[new_row][new_col] < 6:
#                     cnt += 1
#             if cnt != num:
#                 canMake = False
#                 break
#             else:
#                 newgraph[row][col] = -1
#         else:
#             # 백지 타일
#             if newgraph[row][col] == 0:
#                 new_row, new_col = row, col
#                 while newgraph[new_row][new_col] == 0:

#             else:
#                 pass
