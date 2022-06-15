import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
printed = [0 for _ in range(N+1)]

for _ in range(M):
    line = list(map(int, input().split()))
    l = line[0]
    if l == 0:
        continue
    for i in range(1, l):
        a = line[i]
        b = line[i+1]
        graph[a].append(b)
        visited[b] += 1


start = deque()
for i in range(1, N+1):

    if visited[i] == 0:
        start.append(i)

answer = []
cnt = 0
l = len(start)
cycle = False

while start:
    now = start.popleft()
    if printed[now] == 1:
        continue

    if visited[now] != 0:
        # 이전 가수가 아직 안나왔으면
        cnt += 1
        if l == cnt:
            cycle = True
            break
        else:
            start.append(now)
            continue

    answer.append(now)
    printed[now] = 1

    for next in graph[now]:
        start.appendleft(next)
        visited[next] -= 1

    l = len(start)
    cnt = 0

if cycle:
    print(0)
else:
    for now in answer:
        print(now)
