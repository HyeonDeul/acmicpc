from collections import deque

N, M, K = map(int, input().split())

soils = [[0]*(N+1)]
for _ in range(N):
    line = [0]
    line.extend(list(map(int, input().split())))
    soils.append(line)

# trees = [[0 for _ in range(N+1)] for _ in range(N+1)]
tree_list = []

for _ in range(M):
    x, y, z = map(int, input().split())
    # trees[x][y] = z
    tree_list.append([z, x, y])


for _ in range(K):
    tree_list.sort()
    for z, x, y in tree_list:
        if soil[x][y] - z < 0:
