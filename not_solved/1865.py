import sys

for _ in range(int(sys.stdin.readline())):
    N, M, W = map(int, sys.stdin.readline().split())
    graph = {i: {} for i in range(1, N+1)}

    for _ in range(M):
        S, E, T = map(int, sys.stdin.readline().split())
        if E not in graph[S]:
            graph[S][E] = T
        elif graph[S][E] > T:
            graph[S][E] = T
        if S not in graph[E]:
            graph[E][S] = T
        elif graph[E][S] > T:
            graph[E][S] = T
    for _ in range(W):
        S, E, T = map(int, sys.stdin.readline().split())
        # 틀리면 시간 갱신
        graph[S][E] = T

    # 벨만 -포드 알고리즘 공부하기
