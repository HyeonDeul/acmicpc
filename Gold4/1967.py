import sys
from collections import deque

N = int(sys.stdin.readline())

tree = {i: [] for i in range(1, N+1)}

for _ in range(N-1):
    x, y, d = map(int, sys.stdin.readline().split())
    tree[x].append([y, d])
    tree[y].append([x, d])

radius = 0

for i in range(1, N+1):
    if len(tree[i]) == 1:
        queue = deque([[i, -1, 0]])

        while queue:
            now, prev, dis = queue.pop()

            if prev != -1 and len(tree[now]) == 1:
                if radius < dis:
                    radius = dis
            else:
                for next, next_dis in tree[now]:
                    if next != prev:
                        queue.append([next, now, dis+next_dis])

print(radius)
