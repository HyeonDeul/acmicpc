import heapq
mycountry = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}


def dijkstra(road, start):

    country = {node: float('inf') for node in road}
    country[start] = 0
    heap = []
    heapq.heappush(heap, [country[start], start])

    while heap:
        current_distance, now_position = heapq.heappop(heap)

        if country[now_position] < current_distance:
            continue

        for arrival, weight in road[now_position].items():
            distance = current_distance + weight

            if distance < country[arrival]:
                country[arrival] = distance
                heapq.heappush(heap, [distance, arrival])

    return country


dijkstra(mycountry, 'A')

heap_items = [1, 3, 5, 7, 9]

max_heap = []
for item in heap_items:
    heapq.heappush(max_heap, (-item, item))

print(max_heap)
# 최대힙

N = int(input())
arr = list(map(int, input().split()))

dp_orm = [1 for _ in range(N)]
dp_nrm = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp_orm[i] = max(dp_orm[i], dp_orm[j]+1)
        if arr[N-i-1] > arr[N-j-1]:
            dp_nrm[N-i-1] = max(dp_nrm[N-i-1], dp_nrm[N-j-1]+1)

max_arr = 0
for i in range(N):
    arrLen = dp_orm[i]+dp_nrm[i]-1
    if max_arr < arrLen:
        max_arr = arrLen
print(max_arr)
