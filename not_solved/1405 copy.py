# from collections import deque
# import copy

# com, E, W, S, N = map(int, input().split())

# direction = [E/100, W/100, S/100, N/100]
# drow = [0, 0, 1, -1]
# dcol = [1, -1, 0, 0]

# graph = [[0 for _ in range(30)] for _ in range(30)]
# row, col = 14, 14
# graph[row][col] = 1

# que = deque([[0, row, col, 1, graph]])

# answer = 0

# while que:
#     cnt, row, col, per, visit = que.popleft()
#     if cnt == com:
#         answer += per
#         continue
#     cnt += 1

#     for i in range(4):
#         if direction[i] != 0:
#             next_row = row+drow[i]
#             next_col = col+dcol[i]

#             if visit[next_row][next_col] == 0:
#                 temp = copy.deepcopy(visit)
#                 temp[next_row][next_col] = 1
#                 que.append([cnt, next_row, next_col, per*direction[i], temp])

# print(answer)
print(4**14)
