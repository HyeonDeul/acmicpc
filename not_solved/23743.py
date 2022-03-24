import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
warps = {i: {} for i in range(N+1)}

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    if b in warps[a]:
        if warps[a][b] > c:
            warps[a][b] = c
    else:
        warps[a][b] = c
    if a in warps[b]:
        if warps[b][a] > c:
            warps[b][a] = c
    else:
        warps[b][a] = c

escapes = list(map(int, sys.stdin.readline().split()))
for i in range(N):
    warps[0][i+1] = escapes[i]
    warps[i+1][0] = escapes[i]

totalTime = 0


print(totalTime)
