from collections import deque

n, k = map(int, input().split())
graph = [float('inf')] * 200000
queue = deque([[n, 0]])
graph[n] = 0

while queue:
    now, time = queue.popleft()
    if graph[now] < time:
        continue
    if now == 0:
        nexts = [now+1]
    elif now < k:
        nexts = [now-1, now+1, now*2]
    else:
        nexts = [now-1]
    for next in nexts:
        if next == now*2:
            if graph[next] >= time:
                graph[next] = time
                queue.append([next, time])
        elif graph[next] > time+1:
            graph[next] = time+1
            queue.append([next, time+1])

print(graph[k])
