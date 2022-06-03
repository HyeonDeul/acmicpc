import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

before = []
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1 = x1-1, y1-1
    s = 0
    for row in range(x1, x2):
        s += sum(graph[row][y1:y2])
    print(s)
