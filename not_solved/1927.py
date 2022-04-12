import sys
import heapq

N = int(sys.stdin.readline())
queue = []
for _ in range(N):
    t = int(sys.stdin.readline())
    if t == 0:
        if len(queue) == 0:
            print(0)
        else:
            a = heapq.heappop(queue)
            print(a)
    else:
        heapq.heappush(queue, t)
