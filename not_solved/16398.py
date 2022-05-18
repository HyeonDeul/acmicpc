import sys
from collections import deque
import heapq
input = sys.stdin.readline

N = int(input())

que = []
for i in range(N):
    temp = list(map(int, input().split()))

    for j in range(i+1, N):
        heapq.heappush(que, [temp[j], i, j])
print(que)
