import sys
import heapq


def route(graph, start):
    distances = {}
    nodes = {}
    for i in graph:
        distances[i] = float('inf')
        nodes[i] = []

    distances[start] = 0

    queue = [[0, start]]

    while queue:
        now_distance, now_city = heapq.heappop(queue)

        if now_distance > distances[now_city]:
            continue

        for new_city, distance in graph[now_city]:
            new_distance = distance+now_distance
            if new_distance < distances[new_city]:
                distances[new_city] = new_distance
                # nodes[new_city].extend(nodes[now_city])
                nodes[new_city] = now_city
                heapq.heappush(queue, [new_distance, new_city])
    return distances, nodes


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = {i: [] for i in range(1, n+1)}
for _ in range(m):
    x, y, v = map(int, sys.stdin.readline().split())
    graph[x].append([y, v])
start, end = map(int, sys.stdin.readline().split())

distance, node = route(graph, start)

answer = [str(end)]
i = end
while True:
    i = node[i]
    answer.append(str(i))
    if i == start:
        break
answer.reverse()

print(distance[end])
print(len(answer))
print(' '.join(answer))
