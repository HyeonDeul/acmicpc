import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
revered_graph = [[] for _ in range(N+1)]
printed = [0 for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    revered_graph[b].append(a)


nonlist = []
start = deque()
for i in range(1, N+1):
    if len(revered_graph[i]) == 0:
        if len(graph[i]) == 0:
            nonlist.append(i)
            printed[i] = 1
        else:
            start.append(i)

while start:
    i = start.popleft()
    # 이미 출력됐으면
    if printed[i] == 1:
        continue

    canAnswer = True
    for j in revered_graph[i]:
        if printed[j] == 0:
            canAnswer = False
            break

    # 아직 상위 것이 출력되지 않으면
    if not canAnswer:
        start.append(i)
        continue

    nonlist.append(i)
    printed[i] = 1

    for j in graph[i]:
        start.appendleft(j)

print(*nonlist)
