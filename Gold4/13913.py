from collections import deque

n, k = map(int, input().split())
graph = [float('inf')] * 200000
way = [-1] * 200000
queue = deque([[n, 0]])
graph[n] = 0

while queue:
    now, time = queue.popleft()
    if graph[now] < time:
        continue
    if now < k:
        nexts = [now-1, now+1, now*2]
    else:
        nexts = [now-1]
    for next in nexts:
        if next == -1:
            continue
        if graph[next] > time+1:
            graph[next] = time+1
            way[next] = now
            queue.append([next, time+1])

print(graph[k])
answer = str(k)
now = k
while now != n:
    answer = str(way[now]) + ' ' + answer
    now = way[now]
print(answer)
