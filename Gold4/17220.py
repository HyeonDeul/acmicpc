import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

graph = {i: [] for i in range(N)}
reverse = {i: [] for i in range(N)}
# 'A' = 65
for _ in range(M):
    x, y = map(str, input().rstrip().split())
    graph[ord(x)-65].append(ord(y)-65)
    reverse[ord(y)-65].append(ord(x)-65)

police = list(map(str, input().rstrip().split()))
del police[0]
new_police = []
for i in police:
    for j in reverse[ord(i)-65]:
        graph[j].remove(ord(i)-65)
    del graph[ord(i)-65]
    new_police.append(ord(i)-65)

origin = []
for i in range(N):
    if len(reverse[i]) == 0:
        origin.append(i)

cnt = 0
visit = []
que = deque()

for i in origin:
    if i in new_police:
        continue
    que.append(i)

    while que:
        now = que.pop()
        for next in graph[now]:
            if next not in visit:
                visit.append(next)
                que.append(next)

print(len(visit))
