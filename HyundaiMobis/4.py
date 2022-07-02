from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

answer = 0

visit = [[0 for _ in range(M)] for _ in range(N)]


def DFS(row, col):
    que = deque([[row, col]])

    drow = [-1, 0, 1, 0]
    dcol = [0, 1, 0, -1]

    point = 0

    while que:
        row, col = que.pop()
        if visit[row][col] == 1:
            continue
        visit[row][col] = 1

        if graph[row][col] == 0:
            point += 1
        elif graph[row][col] == 2:
            point -= 2

        for i in range(4):
            next_row = row+drow[i]
            if not 0 <= next_row < N:
                continue
            next_col = col+dcol[i]
            if not 0 <= next_col < M:
                continue

            if visit[next_row][next_col] == 0 and graph[next_row][next_col] != 1:
                que.append([next_row, next_col])

    return point if point > 0 else 0


for row in range(N):
    for col in range(M):
        if visit[row][col] == 1:
            continue
        elif graph[row][col] == 1:
            continue

        answer = max(DFS(row, col), answer)

print(answer)

# 주차 시스템
# 치즈 문제 처럼 구역 찾기
