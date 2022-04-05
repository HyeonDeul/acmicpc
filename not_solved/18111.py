import sys

N, M, B = map(int, sys.stdin.readline().split())
graph = []
maxHeight = -1
minHeight = 257
for _ in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    maxHeight = max(maxHeight, max(line))
    minHeight = min(minHeight, min(line))
    graph.append(line)

# 제거 2초
# 삽입 1초
ans = float('inf')
ans_height = -1
for height in range(minHeight, maxHeight+1):
    temp = 0
    can = B
    for line in graph:
        for i in line:
            if height-i > 0:
                temp += height-i
                can -= height-i
            else:
                temp += -2*(height-i)
                can -= height-i
    if temp <= ans and can >= 0:
        ans_height = height
        ans = temp
print(ans, ans_height)
