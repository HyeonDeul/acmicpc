import sys

for _ in range(int(sys.stdin.readline())):
    N, M, W = map(int, sys.stdin.readline().split())
    graph = {i: [] for i in range(1, N+1)}
    for _ in range(M):
        S, E, T = map(int, sys.stdin.readline().split())
        graph[S].append([E, T])
        graph[E].append([S, T])
    for _ in range(W):
        S, E, T = map(int, sys.stdin.readline().split())
        graph[S].append([E, T])
