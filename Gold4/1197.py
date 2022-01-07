from collections import deque

V, E = map(int, input().split())

graph = {i: [] for i in range(1, V+1)}

for _ in range(E):
    a, b, c = map(int, input().split())

    graph[a].append([b, c])
    graph[b].append([a, c])
