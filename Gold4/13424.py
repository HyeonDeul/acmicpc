import heapq


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [0, start])

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        for new_node, new_distance in graph[current_node]:
            distance = current_distance + new_distance
            if distance < distances[new_node]:
                distances[new_node] = distance
                heapq.heappush(queue, [distance, new_node])

    return distances


for _ in range(int(input())):
    N, M = map(int, input().split())

    graph = {i: [] for i in range(1, N+1)}

    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a].append([b, c])
        graph[b].append([a, c])

    cntFriends = int(input())
    friends = list(map(int, input().split()))

    sumOfDistance = [0 for _ in range(N+1)]
    sumOfDistance[0] = float('inf')

    for f in friends:
        distance = dijkstra(graph, f)
        for i in range(1, N+1):
            sumOfDistance[i] += distance[i]

    print(sumOfDistance.index(min(sumOfDistance)))
