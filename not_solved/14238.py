from collections import deque

graph = {'A': 0, 'B': 0, 'C': 0}

works = list(map(str, input()))
days = len(works)

for w in works:
    graph[w] += 1
cba = 0
for i in graph:
    cba = min(cba, graph[i])

answer = 'CBA'*cba
canMake = False
que = deque()
if graph['A'] > 0:
    que.append(['A', 1, 0, 0])
if graph['B'] > 0:
    que.append(['B', 0, 1, 0])
if graph['C'] > 0:
    que.append(['C', 0, 0, 1])

while que:
    now, a, b, c = que.pop()
    l = a+b+c
    if l == days:
        answer = now
        canMake = True
        break
    if graph['A']-a > 0:
        que.append([now+'A', a+1, b, c])
    if graph['B']-b > 0 and now[l-1] != 'B':
        que.append([now+'B', a, b+1, c])
    if graph['C']-c > 0 and now[l-1] != 'C':
        if l >= 2:
            if now[l-2] != 'C':
                que.append([now+'C', a, b, c+1])
        else:
            que.append([now+'C', a, b, c+1])

print(answer if canMake else -1)
