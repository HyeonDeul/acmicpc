
from collections import deque

graph = {'A': 0, 'B': 0, 'C': 0}

works = list(map(str, input()))
days = len(works)

for w in works:
    graph[w] += 1

answer = ''
canMake = False
que = deque()
a, b, c = graph['A'], graph['B'], graph['C']

if graph['A'] > 0:
    que.append(['A', a-1, b, c])
if graph['B'] > 0:
    que.append(['B', a, b-1, c])
if graph['C'] > 0:
    que.append(['C', a, b, c-1])


def func(work, la, lb, lc):
    if not canMake:
        l = la+lb+lc
        if l == days:
            answer = work
            canMake = True
        else:
            if b > 0 and work[l-1] != 'B':
                func(work+'B', a, b-1, c)
            if c > 0 and work[l-1] != 'C':
                if l >= 2:
                    if work[l-2] != 'C':
                        func(work+'C', a, b, c-1)
                else:
                    func(work+'C', a, b, c-1)


while que:
    now, a, b, c = que.pop()
    l = a+b+c
    if l == days:
        answer = now
        canMake = True
        break
    if graph['B']-b > 0 and now[l-1] != 'B':
        que.append([now+'B', a, b+1, c])
    if graph['C']-c > 0 and now[l-1] != 'C':
        if l >= 2:
            if now[l-2] != 'C':
                que.append([now+'C', a, b, c+1])
        else:
            que.append([now+'C', a, b, c+1])
    if graph['A']-a > 0:
        que.append([now+'A', a+1, b, c])


print(answer if canMake else -1)
