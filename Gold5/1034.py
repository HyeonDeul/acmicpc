graph = {}

row, col = map(int, input().split())
for _ in range(row):
    temp = input()
    if temp not in graph:
        graph[temp] = 1
    else:
        graph[temp] += 1

count = int(input())

answer = []

for i in graph:
    zeroCount = i.count('0')
    if zeroCount > count:
        answer.append(0)
    else:
        tempcount = count - zeroCount
        if tempcount % 2 == 1:
            answer.append(0)
        else:
            answer.append(graph[i])

print(max(answer))
