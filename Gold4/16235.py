import sys
from collections import deque


N, M, K = map(int, sys.stdin.readline().split())

soils = []
S2D2 = []
trees = [[deque() for _ in range(N)]for _ in range(N)]

for _ in range(N):
    S2D2.append(list(map(int, sys.stdin.readline().split())))
    soils.append([5]*N)

for _ in range(M):
    x, y, z = map(int, sys.stdin.readline().split())
    trees[x-1][y-1].append(z)


drow = [-1, -1, -1, 0, 1, 1, 1, 0]
dcol = [-1, 0, 1, 1, 1, 0, -1, -1]

for _ in range(K):

    for x in range(N):
        for y in range(N):
            tree = deque()
            add = 0
            for z in trees[x][y]:
                if soils[x][y] >= z:
                    soils[x][y] -= z
                    tree.append(z+1)
                else:
                    add += z//2
            soils[x][y] += add
            trees[x][y] = tree

    temp = []
    for x in range(N):
        for y in range(N):
            for z in trees[x][y]:
                if z % 5 == 0:
                    for i in range(8):
                        next_x = x+drow[i]
                        if not 0 <= next_x < N:
                            continue
                        next_y = y+dcol[i]
                        if not 0 <= next_y < N:
                            continue
                        temp.append((next_x, next_y))
            soils[x][y] += S2D2[x][y]

    for x, y in temp:
        trees[x][y].appendleft(1)

l = 0
for x in range(N):
    for y in range(N):
        l += len(trees[x][y])
print(l)
